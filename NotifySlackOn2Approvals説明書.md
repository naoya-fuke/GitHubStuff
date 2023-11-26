# GitHub Actionsを使用したSlack通知の設定

このドキュメントでは、GitHub Actionsを使用して、プルリクエストが2回承認されたときにSlackに通知を送信する方法について説明します。

## ステップ1: GitHub Secretsの設定

GitHubリポジトリの設定にアクセスし、「Secrets」セクションで新しいSecretを作成します。名前には`SLACK_WEBHOOK_URL_2APPROVE`を使用し、値にはSlack Webhook URLを入力します。

## ステップ2: ワークフローファイルの作成

リポジトリの`.github/workflows`ディレクトリ内に新しいワークフローファイルを作成します。例えば、ファイル名を`notify_slack.yml`とします。

## ステップ3: ワークフローの定義

ワークフローは以下のように定義します。

```yaml
name: Notify Slack on 2 Approvals

on:
  pull_request_review:
    types: [submitted]

jobs:
  notify-slack:
    runs-on: ubuntu-latest
    steps:
      - name: Check for 2 approvals
        id: approvals
        run: |
          # GitHubのレビューAPIエンドポイント
          REVIEW_API_URL="https://api.github.com/repos/${{ github.repository }}/pulls/${{ github.event.pull_request.number }}/reviews"

          # GitHub APIを使用してレビューデータを取得
          reviews=$(curl -s -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" $REVIEW_API_URL)

          # 承認のカウント
          approve_count=$(echo "$reviews" | jq '[.[] | select(.state == "APPROVED")] | length')

          # 環境変数に承認数をセット
          echo "approve_count=$approve_count" >> $GITHUB_ENV

      - name: Send notification to Slack
        if: env.approve_count == '2'
        env:
          PR_URL: ${{ github.event.pull_request.html_url }}
        run: |
          curl -X POST -H 'Content-type: application/json' --data '{"2approve_PR-url": "'"$PR_URL"'"}' ${{ secrets.SLACK_WEBHOOK_URL_2APPROVE }}
