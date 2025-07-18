"""
ゲーム木のパースに必要な抽象化されたメソッドを提供するモジュール
"""
from node import Node


class GameParser:
    """ゲーム文字列をパースするための抽象化されたパーサクラス"""
    
    @staticmethod
    def split_options(options_str):
        """
        ネストされた括弧を考慮して、トップレベルの選択肢をカンマで分割するヘルパー関数。
        """
        options = []
        current_option = ""
        brace_level = 0
        options_str = options_str.strip()

        for char in options_str:
            if char == '{':
                brace_level += 1
            elif char == '}':
                brace_level -= 1
            elif char == ',' and brace_level == 0:
                # トップレベルのカンマで分割
                if current_option.strip():
                    options.append(current_option.strip())
                current_option = ""
                continue
                
            current_option += char
        
        # 最後の選択肢を追加
        if current_option.strip():
            options.append(current_option.strip())
            
        return options
    
    @staticmethod
    def create_simple_node(name):
        """単純なノードを作成"""
        return Node(name)
    
    @staticmethod
    def create_binary_node(name, left_child=None, right_child=None):
        """左右の子を持つバイナリノードを作成"""
        node = Node(name)
        if left_child:
            node.add_left_child(left_child)
        if right_child:
            node.add_right_child(right_child)
        return node
    
    @staticmethod
    def create_recursive_nim_node(k, parse_func):
        """
        *k形式のニム値ノードを再帰的に作成
        *k = {*0,*1,...,*(k-1) | *0,*1,...,*(k-1)}
        """
        if k == 0:
            return Node("0")
        
        root = Node(f"*{k}")
        left_children = []
        right_children = []
        
        # 左右の選択肢: *0, *1, ..., *(k-1)
        for i in range(k):
            left_children.append(parse_func(f"*{i}"))
            right_children.append(parse_func(f"*{i}"))
        
        root.set_left_children(left_children)
        root.set_right_children(right_children)
        return root
    
    @staticmethod
    def create_up_node(parse_func):
        """↑ = {0 | *1} ノードを作成"""
        return GameParser.create_binary_node(
            "↑",
            left_child=Node("0"),
            right_child=parse_func("*1")
        )
    
    @staticmethod
    def create_down_node(parse_func):
        """↓ = {*1 | 0} ノードを作成"""
        return GameParser.create_binary_node(
            "↓",
            left_child=parse_func("*1"),
            right_child=Node("0")
        )
    
    @staticmethod
    def parse_n_times_up(game_string, parse_func):
        """
        n × ↑ 形式をパース
        n × ↑ = {0 | (n-1) × ↑ + *}
        """
        parts = game_string.split('×')
        if len(parts) != 2:
            raise ValueError(f"Invalid n × ↑ format: '{game_string}'")
        
        try:
            n = int(parts[0].strip())
        except ValueError:
            raise ValueError(f"Invalid number in n × ↑ format: '{parts[0].strip()}'")
        
        if n == 1:
            return GameParser.create_up_node(parse_func)
        
        root = Node(f"{n} × ↑")
        left_child = Node("0")
        
        # 右側: (n-1) × ↑ + *
        if n - 1 == 1:
            right_child = GameParser.create_up_plus_star_base(parse_func)
        else:
            right_child = GameParser.create_n_up_plus_star_node(n - 1, parse_func)
        
        root.add_left_child(left_child)
        root.add_right_child(right_child)
        return root
    
    @staticmethod
    def parse_n_times_up_plus_star(game_string, parse_func):
        """
        n × ↑ + * 形式をパース
        n × ↑ + * = {0 | (n - 1) × ↑}
        """
        parts = game_string.split('×')
        if len(parts) != 2:
            raise ValueError(f"Invalid n × ↑ + * format: '{game_string}'")
        
        try:
            n = int(parts[0].strip())
        except ValueError:
            raise ValueError(f"Invalid number in n × ↑ + * format: '{parts[0].strip()}'")
        
        return GameParser.create_n_up_plus_star_node(n, parse_func)
    
    @staticmethod
    def create_n_up_plus_star_node(n, parse_func):
        """n × ↑ + * ノードを作成"""
        if n == 1:
            return GameParser.create_up_plus_star_base(parse_func)
        
        root = Node(f"{n} × ↑ + *")
        left_child = Node("0")
        
        # 右側: (n - 1) × ↑
        if n - 1 == 1:
            right_child = GameParser.create_up_node(parse_func)
        else:
            right_child = parse_func(f"{n - 1} × ↑")
        
        root.add_left_child(left_child)
        root.add_right_child(right_child)
        return root
    
    @staticmethod
    def create_up_plus_star_base(parse_func):
        """
        基底ケース: ↑ + * = {0, * | 0}
        """
        root = Node("↑ + *")
        
        left_children = [Node("0"), parse_func("*1")]
        right_children = [Node("0")]
        
        root.set_left_children(left_children)
        root.set_right_children(right_children)
        return root
    
    @staticmethod
    def negate_game(node, parse_func):
        """
        ゲーム局面を反転させる操作
        左右の子を入れ替え、再帰的に子ノードも反転する
        """
        if node is None:
            return None
        
        # 0は反転しても0のまま
        if node.name == "0":
            return Node("0")
        
        # 新しいノードを作成（名前に-を付ける）
        negated_node = Node(f"-{node.name}")
        
        # 左右を入れ替えて再帰的に反転
        negated_left_children = []
        negated_right_children = []
        
        # 元の右の子 → 新しい左の子
        for right_child in node.right_children:
            negated_left = GameParser.negate_game(right_child, parse_func)
            negated_left_children.append(negated_left)
        
        # 元の左の子 → 新しい右の子
        for left_child in node.left_children:
            negated_right = GameParser.negate_game(left_child, parse_func)
            negated_right_children.append(negated_right)
        
        # setメソッドを使用して子ノードを設定
        negated_node.set_left_children(negated_left_children)
        negated_node.set_right_children(negated_right_children)
        
        return negated_node
    
    @staticmethod
    def parse_bracket_notation(game_string, parse_func):
        """
        括弧記法 { ... | ... } をパース
        """
        if not game_string.startswith('{') or not game_string.endswith('}'):
            raise ValueError(f"Invalid game format: '{game_string}' does not start with '{{' or end with '}}'")

        root = Node(game_string)
        content = game_string[1:-1].strip()
        
        if not content:
            return root

        # '|'を探してleft/rightに分割
        brace_level = 0
        split_index = -1
        for i, char in enumerate(content):
            if char == '{':
                brace_level += 1
            elif char == '}':
                brace_level -= 1
            elif char == '|' and brace_level == 0:
                split_index = i
                break
                
        if split_index == -1:
            raise ValueError(f"Invalid game format: Separator '|' not found at top level in '{content}'")

        left_part_str = content[:split_index].strip()
        right_part_str = content[split_index + 1:].strip()
        
        # 左の選択肢をパース
        if left_part_str:
            left_options = GameParser.split_options(left_part_str)
            left_children = [parse_func(option_str) for option_str in left_options]
            root.set_left_children(left_children)
            
        # 右の選択肢をパース
        if right_part_str:
            right_options = GameParser.split_options(right_part_str)
            right_children = [parse_func(option_str) for option_str in right_options]
            root.set_right_children(right_children)

        return root
    
    @staticmethod
    def create_integer_node(n, parse_func):
        """
        整数nに対応するゲーム木を作成
        n = {n-1 | } (n > 0)
        0 = { | } (基底ケース)
        """
        if n == 0:
            return Node("0")
        
        if n < 0:
            raise ValueError(f"Negative integers are not supported: {n}")
        
        root = Node(str(n))
        
        # 左の子: n-1
        left_child = GameParser.create_integer_node(n - 1, parse_func)
        root.add_left_child(left_child)
        
        # 右の子: なし（空）
        return root


class TreeVisualizer:
    """ゲーム木の可視化を行うクラス"""
    
    @staticmethod
    def print_tree_enhanced(node, prefix="", is_last=True, is_left=None, level=0):
        """
        改良されたテキスト形式での木構造表示
        """
        if node is None: 
            return
        
        # インデントと接続線の設定
        if level == 0:
            # ルートノード
            print(f"🎯 ROOT: {node.name}")
        else:
            # 子ノード
            connector = "└── " if is_last else "├── "
            side_indicator = "⬅️ LEFT" if is_left else "➡️ RIGHT"
            print(f"{prefix}{connector}{side_indicator}: {node.name}")
        
        # 子ノードの前置詞を決定
        new_prefix = prefix + ("    " if is_last else "│   ")
        
        # 左右の子ノードの総数を取得
        total_children = len(node.left_children) + len(node.right_children)
        current_child_index = 0
        
        # 左の子ノードを表示
        for i, left_child in enumerate(node.left_children):
            is_last_child = (current_child_index == total_children - 1)
            TreeVisualizer.print_tree_enhanced(
                left_child, new_prefix, is_last_child, is_left=True, level=level+1
            )
            current_child_index += 1
        
        # 右の子ノードを表示
        for i, right_child in enumerate(node.right_children):
            is_last_child = (current_child_index == total_children - 1)
            TreeVisualizer.print_tree_enhanced(
                right_child, new_prefix, is_last_child, is_left=False, level=level+1
            )
            current_child_index += 1
    
    @staticmethod
    def print_tree_compact(node):
        """
        コンパクトな形式での木構造表示
        """
        def format_node_compact(node, depth=0):
            if node is None:
                return ""
            
            indent = "  " * depth
            result = f"{indent}{node.name}\n"
            
            # 左の子を表示
            if node.left_children:
                result += f"{indent}├─ LEFT:\n"
                for child in node.left_children:
                    result += format_node_compact(child, depth + 2)
            
            # 右の子を表示
            if node.right_children:
                result += f"{indent}└─ RIGHT:\n"
                for child in node.right_children:
                    result += format_node_compact(child, depth + 2)
            
            return result
        
        print("📊 COMPACT TREE VIEW:")
        print(format_node_compact(node))
    
    @staticmethod
    def generate_dot_graph(node, filename="game_tree", keep_dot=False):
        """
        DOT形式のグラフを生成し、直接PNGに変換
        """
        import subprocess
        import os
        
        dot_content = ["digraph GameTree {"]
        dot_content.append("  rankdir=TB;")
        dot_content.append("  node [shape=box, style=rounded];")
        
        node_counter = [0]  # カウンターを参照渡しで使用
        
        def add_node_to_dot(node, parent_id=None, is_left=None):
            if node is None:
                return
            
            current_id = f"node{node_counter[0]}"
            node_counter[0] += 1
            
            # ノードのラベルと色を設定
            label = node.name.replace('"', '\\"')
            color = "#E3F2FD"  # デフォルト色
            
            if node.name == "0":
                color = "#FFEBEE"  # 薄い赤
            elif node.name.startswith("*"):
                color = "#E8F5E8"  # 薄い緑
            elif node.name in ["↑", "↓"]:
                color = "#FFF3E0"  # 薄いオレンジ
            
            dot_content.append(f'  {current_id} [label="{label}", fillcolor="{color}", style=filled];')
            
            # 親ノードとの接続
            if parent_id is not None:
                edge_label = "LEFT" if is_left else "RIGHT"
                edge_color = "blue" if is_left else "red"
                dot_content.append(f'  {parent_id} -> {current_id} [label="{edge_label}", color={edge_color}];')
            
            # 左の子ノードを追加
            for child in node.left_children:
                add_node_to_dot(child, current_id, is_left=True)
            
            # 右の子ノードを追加
            for child in node.right_children:
                add_node_to_dot(child, current_id, is_left=False)
        
        add_node_to_dot(node)
        dot_content.append("}")
        
        # DOTファイルに書き込み
        dot_filename = f"{filename}.dot"
        png_filename = f"{filename}.png"
        
        with open(dot_filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(dot_content))
        
        print(f"📈 DOT file generated: {dot_filename}")
        
        # Graphvizでpngに変換
        try:
            result = subprocess.run([
                'dot', '-Tpng', dot_filename, '-o', png_filename
            ], capture_output=True, text=True, check=True)
            
            print(f"🖼️  PNG image generated: {png_filename}")
            
            # DOTファイルを削除（オプション）
            if os.path.exists(png_filename) and not keep_dot:
                try:
                    os.remove(dot_filename)
                    print(f"🗑️  Temporary DOT file removed: {dot_filename}")
                except OSError:
                    pass
            elif keep_dot:
                print(f"💾 DOT file kept: {dot_filename}")
            
            return png_filename
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Error converting DOT to PNG: {e}")
            print("⚠️  Please make sure Graphviz is installed:")
            print("   Ubuntu/Debian: sudo apt install graphviz")
            print("   macOS: brew install graphviz")
            print("   Windows: Download from https://graphviz.org/download/")
            return dot_filename
            
        except FileNotFoundError:
            print("❌ Graphviz 'dot' command not found!")
            print("⚠️  Please install Graphviz:")
            print("   Ubuntu/Debian: sudo apt install graphviz")
            print("   macOS: brew install graphviz") 
            print("   Windows: Download from https://graphviz.org/download/")
            return dot_filename
    
    @staticmethod
    def print_game_notation(node):
        """
        ゲーム記法での表示
        """
        def format_game_notation(node):
            if node is None:
                return ""
            
            if node.name == "0":
                return "0"
            
            # 左右の子をゲーム記法で表現
            left_parts = []
            right_parts = []
            
            for child in node.left_children:
                left_parts.append(format_game_notation(child))
            
            for child in node.right_children:
                right_parts.append(format_game_notation(child))
            
            left_str = ", ".join(left_parts) if left_parts else ""
            right_str = ", ".join(right_parts) if right_parts else ""
            
            return f"{{{left_str} | {right_str}}}"
        
        notation = format_game_notation(node)
        print(f"🎮 GAME NOTATION: {notation}")
