GitHub Desktopを使用している場合でも、Visual Studio Code（VS Code）の統合ターミナルを利用してGitコマンドを実行することは可能です。VS Codeは、Git操作を簡単に行える強力なエディターであり、GitHub Desktopと併用することで開発ワークフローを効率化できます。



GitHub DesktopとVS Codeを連携させる
GitHub Desktopでプロジェクトを管理しながら、VS Codeでコードの編集やターミナルでのGit操作を行いたい場合、以下の手順を踏むことでセットアップできます。

1. GitHub Desktopでリポジトリを開く
GitHub Desktopで操作したいリポジトリを選択し、リポジトリメニュー（または右クリックメニュー）から「Open in Visual Studio Code」を選択します。これにより、VS Codeでそのリポジトリが開かれます。

2. VS Codeでターミナルを開く
VS Codeには統合ターミナルがあります。これを開くには、メニューバーから「Terminal」＞「New Terminal」を選択するか、ショートカットCtrl+`（バッククオートキー）を使用します。

3. ターミナルでGitコマンドを使用する
VS Codeのターミナルが開けば、Gitコマンドを直接実行してリポジトリの管理を行うことができます。例えば、git status、git add、git commit、git pushなどのコマンドを使って、変更のステージング、コミット、リモートへのプッシュを行うことができます。

注意点
GitHub DesktopとVS Codeの統合ターミナルを併用する場合、GitHub Desktopで行った操作はVS Codeに即座に反映されることが多いですが、VS Codeやその他のコマンドラインツールで行った変更はGitHub Desktopに反映されるまで少し時間がかかる場合があります。そのため、両方のツールを同時に使用する際には、最新の状態に同期されていることを確認することが重要です。
VS CodeにはGit操作を簡単に行うためのGUIが組み込まれていますが、ターミナルを使うことでより詳細なGitコマンドを実行できます。
GitHub DesktopとVS Codeの組み合わせは、Gitリポジトリの管理とコード編集をスムーズに行うための強力なツールセットを提供します。VS Codeのターミナルを活用することで、GitHub DesktopのGUIだけでは実現できないより高度なGit操作も行えるようになります。

 # GitHubStuff
GitHubにまつわる事をなんでもあげていく。  

## どうやるとrevertができなくなるのだ？
cmdからコードをあげるテストをしたり、気になって調べたことを書いていくリポジトリだぜ！！!！！！！！


## 後でまとめる
GITHUBのトークンから、それが誰かを確認する方法

```
$  curl -H "Authorization: Bearer ${T_GITHUB_API_TOKEN}" https://api.github.com/user
```

でscopeと作ったuserがわかる

色々追加するとrevertできなくなるのかな

色々書き足してrevertできなくなるか見る

