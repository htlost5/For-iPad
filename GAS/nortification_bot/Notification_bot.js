function sendLineMessage() {
  var token = "f8orYBtPlqp1KK3pigFCflyAQI68SIeg2tK3VDl5dwA";
  var today = new Date();
  var month = parseInt(Utilities.formatDate(today, "Asia/Tokyo", "M"), 10)
  var day = today.getDate();

  var sheetValue;
  switch (month) {
    case 4:
    sheetValue = "A3:G7"
    break;

    case 5:
    sheetValue = "A12:G16"
    break;

    case 6:
    sheetValue = "A21:G25"
    break;

    case 7:
    sheetValue = "A31:G35"
    break;

    case 8:
    sheetValue = "A40:G44"
    break;

    case 9:
    sheetValue = "A49:G53"
    break;
    
    case 10:
    sheetValue = "A58:G62"
    break;

    case 11:
    sheetValue = "A67:G73"
    break;

    case 12:
    sheetValue = "A76:G80"
    break;

    case 1:
    sheetValue = "A85:G89"
    break;

    case 2:
    sheetValue = "A94:G98"
    break;

    case 3:
    sheetValue = "A103:G108"
    break;
  }

  var foundCells = findExactNumber("シート1", sheetValue, day)
  Logger.log(foundCells);
  
  var message = month + sheetValue
  
  var options = {
    "method": "post",
    "headers": {"Authorization": "Bearer " + token},
    "payload": {"message": message},
    "muteHttpExceptions": true
  };
  
  try {
    var response = UrlFetchApp.fetch("https://notify-api.line.me/api/notify", options);
    Logger.log("応答コード: " + response.getResponseCode());
    Logger.log("応答内容: " + response.getContentText());
    Logger.log("送信したメッセージ: " + message);
    Logger.log(sheetValue)
  } catch (e) {
    Logger.log("エラー: " + e.toString());
  }
}


function findExactNumber(sheetName, range, targetNumber) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(sheetName);
  var values = sheet.getRange(range).getValues();
  var result = [];

  for (var i = 0; i < values.length; i++) {
    for (var j = 0; j < values[i].length; j++) {
      if (values[i][j] === targetNumber) {
        // 一致する数値が見つかった場合、行番号と列番号を保存
        result.push({ row: i + 1, column: j + 1, value: values[i][j] });
      }
    }
  }

  return result;
}
