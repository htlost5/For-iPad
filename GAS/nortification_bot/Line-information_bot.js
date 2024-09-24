const ACCESS_TOKEN = 'm9UJJRGphgqXIv4e8XHYakM5LxDiJ/uRsT0U93CTJXR8P6w+Ryl1eGx/OvPB5oicoffE6ahz8SvpGsMOrevED76i6o1WBwXWlitVByih8wcsN+0ur35F7nSU81MaXQ6Rq0QXGoXKbb7reNyLD1SiyQdB04t89/1O/w1cDnyilFU=';

function doPost(e) {
  const event = JSON.parse(e.postData.contents).events[0];
  const replyToken = event.replyToken;
  let message;

  if (event.type === 'message' && event.message.type === 'text') {
    if (event.source.type === 'group') {
      const groupId = event.source.groupId;
      message = `グループIDは: ${groupId}`;
    } else if (event.source.type === 'user') {
      const userId = event.source.userId;
      message = `ユーザーIDは: ${userId}`;
    } else {
      message = 'このタイプのIDは取得できません。';
    }

    replyMessage(replyToken, message);
  }
}

function replyMessage(replyToken, message) {
  UrlFetchApp.fetch('https://api.line.me/v2/bot/message/reply', {
    'headers': {
      'Content-Type': 'application/json; charset=UTF-8',
      'Authorization': 'Bearer ' + ACCESS_TOKEN,
    },
    'method': 'post',
    'payload': JSON.stringify({
      'replyToken': replyToken,
      'messages': [{
        'type': 'text',
        'text': message,
      }],
    }),
  });
}