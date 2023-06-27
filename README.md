# aminome

**A**dd all **mi**sskey **no**tes to **Me**ilisearch.

## Note

If you import to a new meili_data, you need to run `updateSettings.sh` first to update index settings else you will countered this error:
```
ERR  * [api]   Internal error occurred in notes/search: Attribute `createdAt` is not sortable. This index does not have configured sortable attributes.
```

Run `getSettings.sh` to see current meilisearch index search

## これは何

- [[13.12.0 beta.5]Meilisearchで導入以前の過去のノートを検索できるようにマイグレーションしたい · Issue #10789 · misskey-dev/misskey](https://github.com/misskey-dev/misskey/issues/10789) を実現します。
- 自分のサーバーの全ノート(ローカル)をMeilisearchへ登録します。

## 対象バージョン

- Misskey v13.12.2
- Meilisearch v1.1.1

## 使い方

1. python packageをインストールします。

    ```sh
    pip3 install -r requirements.txt
    ```

2. `aminome.py` を開き、`postgresql config` と `meilisearch config` を設定します。

3. 実行します。

    ```sh
    python3 ./aminome.py
    ```

## 参考実装

- [dump_misskey_note_data.py](https://gist.github.com/CyberRex0/d481c4c2be6dc47fee4b50cefadf2074)
- [mattyatea/misskey-meilisearch-oldnote-index](https://github.com/mattyatea/misskey-meilisearch-oldnote-index)
