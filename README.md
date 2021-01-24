# Simple Thread

![eyecatch](https://cdn.discordapp.com/attachments/752286472383758416/758455916986761256/image0.jpg)

> Simple Thread は Discord サーバーにスレッド機能を追加する bot です。

### **[✉️ Click To Invite !](https://discord.com/api/oauth2/authorize?client_id=754309543160184893&permissions=8&scope=bot)**

## 使い方

### `/set <ThreadMasterChannel> <ThreadCategory> <ArchiveCategory>`

スレッドを設定します。

IDが重複していなければ、いくらでもスレッドを追加できます。

これらの引数はIDで渡してください。名前でも構いませんが、IDの方が確実です。

### `/remove <ThreadMasterChannel>`

setコマンドで保存されているスレッド機能を削除します。

チャンネルやカテゴリは削除されません。

### `<ThreadName>`

これを `<ThreadMasterChannel>` に送ると、Simple Thread が `<ThreadCategory>` の中に `<ThreadName>` という名前のチャンネルを作成します。

Tips: `<ArchiveCategory>` に `<ThreadName>` という名前のチャンネルがある場合は、そのチャンネルをアーカイブから戻します。

### `/reopen`

`<ArchiveCategory>` のチャンネルに送るとスレッドに戻されます。

サーバがアーカイブカテゴリを書き換え不可能にしている場合は、`<ThreadName>`のTipsを参考にしてください。

### `/rename <ThreadName>`

送信されたスレッドのチャンネル名を `<ThreadName>` に変更します。

注意: discord 側の制限により、同じスレッドのチャンネル名は 10 分間に 2 回しか更新されません。

### `/close`

送信先のスレッドを `<ArchiveCategory>` にアーカイブします。

Tips: サーバーの管理者であれば、無差別に閉じることができます。


## その他

### `未読順ソート`

各スレッドは、新しいメッセージが送信されるとスレッドマスターのひとつ下の位置に移動します。

どのチャンネルが更新されたかは気にしないでください。上からタップするだけで最新のメッセージを確認できます。

## 必要な権限

- Administrator (管理者)

### なぜ管理者権限が必要なのか

申し訳ありませんが、この bot は `sync_permission()` メソッドを使用しています。

あまりにも強い権限を要求するこの問題の解決策があれば教えてください。

<hr />

**解決しない or 新しい問題** があれば **Issue** を立てるか、**[Twitter](https://twitter.com/tenzyumasuda)** にダイレクトメッセージを送ってください。気軽にどうぞ！

<br />

<br />

<p align="center">©️ 2020 - 2021 Tenzyu Masuda</p>

<br />

<br />
