# coding: utf-8

# 経路探索関数
def search_goal(start):
    # スタート位置（x座標, y座標, 移動回数）をセット
    pos = start

    while len(pos) > 0:  # 探索可能ならTrue
        h, w, depth = pos.pop(0)  # リストから探索する位置を取得

        # グリッドから出れたら終了
        if maze[h][w] == 1:
            return "YES"

        # 探索済みとしてセット
        maze[h][w] = 2

        # 現在位置の上下左右を探索：〇<2は壁でもなく探索済みでもないものを示す
        if maze[h-1][w] < 2:  # 左
            pos.insert(0, [h-1, w, depth + 1])
        if maze[h+1][w] < 2:  # 右
            pos.insert(0, [h+1, w, depth + 1])
        if maze[h][w-1] < 2:  # 上
            pos.insert(0, [h, w-1, depth + 1])
        if maze[h][w+1] < 2:  # 下
            pos.insert(0, [h, w+1, depth + 1])

    return "NO"


if __name__ == '__main__':
    HW = [int(x) for x in input().split(" ")]
    # グリッドの縦の長さ = H
    H = HW[0]
    # グリッドの横の長さ = W
    W = HW[1]

    # グリッドの状態を２次元配列で作成
    maze = [list(input()) for x in range(H)]

    # スタートの座標を取得
    # +1している理由は次に、グリッドをぐるっと囲って情報を追加するため
    for i, maze_row in enumerate(maze):
        if "S" in maze_row:
            start_w = maze_row.index("S") + 1
            start_h = i + 1

    # グリッドの状態を壁が「9」、それ以外を「0」と変換する
    maze = [[9 if y == "#" else 0 for j,
             y in enumerate(x)] for i, x in enumerate(maze)]

    # グリッドをぐるっと囲うように「1」の要素や行を追加する
    for i in range(H+1):
        if i == 0:
            maze.insert(0, [1 for x in range(W+2)])
        elif i == H:
            maze.append([1 for x in range(W+2)])
            maze[i].insert(0, 1)
            maze[i].append(1)
        else:
            maze[i].insert(0, 1)
            maze[i].append(1)

    start = [[start_h, start_w, 0]]  # スタート位置
    print(search_goal(start))
