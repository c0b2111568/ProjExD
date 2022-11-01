# 第4回
## 逃げろこうかとん（ex04/dodge_bomb.py）
### ゲーム概要
- ex04/dodge_bomb.pyを実行すると，1600x900䛾スクリーンに草原が描画され，こうかとん
を移動させ飛び回る爆弾から逃げるゲーム
- こうかとんが爆弾と接触するとゲームオーバーで終了する
### 操作方法
- 矢印キーでこうかとんを上下左右に移動する
### 追加機能
- BGMを流れるようにした
- 毎回ゲームを開始するたびに爆弾の色が変わるように設定した。（運が悪いと背景と同化して爆弾が見えにくくなる）
- こうかとんと爆弾がぶつかったら効果音がなるようにした
- 壁に爆弾がバウンドするたびに速さが早くなるようにした
- 画面上にマウスポインタが表示されたら消えるようにした
### ToDo（実装しようと思ったけど時間がなかった）
- [ ] 壁に爆弾がバウンドするたびに爆弾の数が増えるように設定したかった
### メモ