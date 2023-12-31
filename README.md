# mypkg

![test](https://github.com/minamimi13/mypkg/actions/workflows/test.yml/badge.svg)

#### ロボットシステム学2023　授業課題用リポジトリ
このリポジトリはtalkerとlistenerとの間で相互通信を行うROS 2のパッケージです。
これには占い結果を表示させるtalkerとlistenerの相互通信が含まれます。

## 目次
* [talker.py](#talkerpy)
* [listener.py](#listenerpy)
* [uranai_talker.py](#uranai_talkerpy)
* [uranai_listener.py](#uranai_listenerpy)
* [talk_listen.launch.py](#talk_listenlaunchpy)
* [トピック](#トピック)
* [コマンドと実行例](#コマンドと実行例)
* [必要なソフトウェア](#必要なソフトウェア)
* [テスト環境](#テスト環境)
* [著作権・ライセンス](#著作権ライセンス)

## talker.py

## listener.py

## uranai_talker.py

## uranai_listener.py

## talk_listen.launch.py

### トピック
### countup

### uranai


## コマンドと実行例
### 例1
#### 端末1
~~~
$ ros2 run mypkg talker
~~~
#### 端末2
~~~
$ ros2 topic echo /countup
~~~
#### 実行結果(端末2(受信側)にて表示)
~~~
data: 147
---
data: 148
---
data: 149
---
data: 150
---
data: 151
---
data: 152
---

~~~

### 例2
#### 端末1
~~~
$ ros2 run mypkg talker
~~~
#### 端末2
~~~
$ ros2 run mypkg listener
~~~

#### 実行結果(端末2(受信側)にて表示)
~~~
[INFO] [1704026666.502306789] [listener]: Listen: 14
[INFO] [1704026666.993708200] [listener]: Listen: 15
[INFO] [1704026667.493440809] [listener]: Listen: 16
[INFO] [1704026667.993638455] [listener]: Listen: 17
[INFO] [1704026668.493509554] [listener]: Listen: 18
[INFO] [1704026668.993572922] [listener]: Listen: 19
~~~

### 例3
#### 端末1
~~~
$ ros2 run mypkg uranai_talker
~~~
#### 端末2
~~~
$ ros2 topic echo /uranai
~~~

#### 実行結果(端末2(受信側)にて表示)
~~~
data: 18
---
data: 7
---
data: 16
---
data: 7
---
data: 14
---
data: 2
---

~~~

### 例4
#### 端末1
~~~
$ ros2 run mypkg uranai_talker
~~~
#### 端末2
~~~
$ ros2 run mypkg uranai_listener
~~~

#### 実行結果(端末2(受信側)にて表示)
~~~
[INFO] [1704028630.930499291] [uranai_listener]: 今日の運勢は磁力的な魅力が湧き出るでしょう

[INFO] [1704028631.345761762] [uranai_listener]: 今日の運勢は重要な出会いがあります

[INFO] [1704028631.845648547] [uranai_listener]: 今日の運勢は行動力の勝利です

[INFO] [1704028632.345773440] [uranai_listener]: 今日の運勢は大きな変化があります

[INFO] [1704028632.845548142] [uranai_listener]: 今日の運勢は情熱と熱意が湧くでしょう

[INFO] [1704028633.345682057] [uranai_listener]: 今日の運勢は名誉と表彰に見回られるでしょう
~~~

### 例5
#### 端末1
~~~
$ ros2 launch mypkg talk_listen.launch.py
~~~
#### 実行結果
~~~
[INFO] [launch]: All log files can be found below /home/kitami/.ros/log/2023-12-31-22-03-33-705358-marine00-24446
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [24448]
[INFO] [listener-2]: process started with pid [24450]
[INFO] [uranai_talker-3]: process started with pid [24452]
[INFO] [uranai_listener-4]: process started with pid [24454]
[listener-2] [INFO] [1704027814.512730805] [listener]: Listen: 2310
[listener-2] [INFO] [1704027814.693029527] [listener]: Listen: 0
[uranai_listener-4] [INFO] [1704027814.760633671] [uranai_listener]: 今日の運勢は健康に注意してください
[uranai_listener-4]
[listener-2] [INFO] [1704027814.994550555] [listener]: Listen: 2311
[listener-2] [INFO] [1704027815.193163402] [listener]: Listen: 1
[uranai_listener-4] [INFO] [1704027815.241231650] [uranai_listener]: 今日の運勢は過激な闘争心が湧くでしょう
[uranai_listener-4]
~~~

## 必要なソフトウェア
* Python
* Ubuntu 20.04.6 LTS
* ROS 2 Foxy

## テスト環境
* 千葉工業大学の上田隆一先生のコンテナを使用し、テストを行っています。
  * [ryuichiueda/ubuntu22.04-ros2](https://hub.docker.com/r/ryuichiueda/ubuntu22.04-ros2)

## 著作権・ライセンス
* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
* このパッケージのコードの一部は、下記のコード（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、本人の許可を得て自身の著作としたものです。[ryuichiueda/robosys2023](https://github.com/ryuichiueda/robosys2023)
#### © 2023 Saori Kitami
