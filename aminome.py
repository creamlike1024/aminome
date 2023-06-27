# Register all notes on Misskey to Meilisearch
import psycopg2
import psycopg2.extras
import orjson
import requests

# postgresql config
db = psycopg2.connect(
    host='localhost',
    user='misskey-user',
    password='password',
    database='misskey',
    port=5432,
    cursor_factory=psycopg2.extras.DictCursor
)

# meilisearch config
api_key = "APIKEY"
index = ""
url = f"http://localhost:7700/indexes/{index}---notes/documents?primaryKey=id"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

lmt = 100000
ofs = 0

while True:
    # Initialize notes from batch
    notes = []

    # Get a batch
    with db.cursor() as cur:
        cur.execute('SELECT "id", "createdAt", "userId", "userHost", "channelId", "cw", "text", "tags" FROM "note" \
                    WHERE ("note"."text" IS NOT NULL) \
                    LIMIT '  + str(lmt) + ' OFFSET ' + str(ofs))
        qnotes = cur.fetchall()
        if not qnotes:
            break
    for note in qnotes:
        notes.append({
            'id': note['id'],
            'createdAt': int(note['createdAt'].timestamp() * 1000),
            'userId': note['userId'],
            'userHost': note['userHost'],
            'channelId': note['channelId'],
            'cw': note['cw'],
            'text': note['text'],
            'tags': note['tags']
        })
    print(f'{ofs=} {lmt=} {len(notes)=}')
    ofs = ofs + lmt

    # Post a batch
    response = requests.post(url, data=orjson.dumps(notes), headers=headers)

    # Print batch result
    print(response.content)

print('All notes uploaded, program finish.')

db.close()
