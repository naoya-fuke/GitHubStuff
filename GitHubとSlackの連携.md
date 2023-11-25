
# GitHubとSlackの連携

SlackとGitHubを連携することで、GitHubのリポジトリのアクティビティをSlackチャンネルで直接追跡することができます。この連携により、チームのコミュニケーションとコラボレーションが向上し、プロジェクトの進捗をリアルタイムで確認することが可能になります。

## GitHubリポジトリのSlackへの購読

GitHubリポジトリのイベントをSlackチャンネルに通知するには、以下のコマンドをSlackの対応するチャンネルで実行します。

```bash
/github subscribe owner/repository issues,pulls,releases,deployments,reviews,comments,branches,commits:*,discussions
```

### コマンドの構成

- `/github subscribe`: GitHubリポジトリを購読するためのコマンド。
- `owner/repository`: 購読したいGitHubリポジトリのオーナー名とリポジトリ名。
- `issues,pulls,releases,deployments,reviews,comments,branches,commits:*,discussions`: 購読するイベントのタイプ。

### 購読可能なイベントの種類

- `issues`: Issueの作成、更新、クローズ。
- `pulls`: プルリクエストの作成、更新、マージ、クローズ。
- `releases`: リリースの公開。
- `deployments`: デプロイメントのステータス。
- `reviews`: プルリクエストのレビュー。
- `comments`: コメントの追加。
- `branches`: ブランチの作成や削除。
- `commits*`: コミットの通知（任意のブランチ）。
- `discussions`: ディスカッションの投稿。

### 注意事項

- SlackとGitHubを連携する前に、SlackにGitHubアプリをインストールしておく必要があります。
- 各イベントタイプは、プロジェクトやチームのニーズに応じてカスタマイズ可能です。
- このコマンドは、実行されたSlackチャンネルでのみ有効です。
- この連携により、GitHubの重要なアップデートをリアルタイムでSlackチャンネルに通知し、チームメンバーとの即時のフィードバックとコミュニケーションが可能になります。
