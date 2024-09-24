function createCalendar() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getActiveSheet();
  
  var months = ['4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月', '1月', '2月', '3月'];
  var daysOfWeek = ['日', '月', '火', '水', '木', '金', '土'];
  
  var currentRow = 1;
  var thursdayCounter = 0; // 木曜日のカウンター
  
  for (var m = 0; m < months.length; m++) {
    sheet.getRange(currentRow, 1).setValue(months[m]);
    currentRow++;
    
    sheet.getRange(currentRow, 1, 1, 7).setValues([daysOfWeek]);
    currentRow++;
    
    var daysInMonth = getDaysInMonth(m);
    var startDay = getStartDay(m);
    
    var calendarData = [];
    var week = new Array(7).fill('');
    var dayCount = 1;
    
    for (var i = 0; i < 6; i++) {
      week = new Array(7).fill('');
      for (var j = 0; j < 7; j++) {
        if (i === 0 && j < startDay) {
          continue;
        }
        if (dayCount > daysInMonth) {
          break;
        }
        week[j] = dayCount++;
      }
      calendarData.push(week);
      if (dayCount > daysInMonth) {
        break;
      }
    }
    
    sheet.getRange(currentRow, 1, calendarData.length, 7).setValues(calendarData);
    
    setCollectionInfo(sheet, currentRow, calendarData, thursdayCounter, months[m]);
    
    currentRow += calendarData.length + 2;
    thursdayCounter += getThursdayCount(calendarData);
  }
}

function getDaysInMonth(monthIndex) {
  var daysInMonth = [30, 31, 30, 31, 31, 30, 31, 30, 31, 31, 28, 31]; // 4月から3月まで
  return daysInMonth[monthIndex];
}

function getStartDay(monthIndex) {
  var startDays = [1, 3, 6, 1, 4, 0, 2, 5, 0, 3, 6, 6]; // 4月から3月までの開始曜日（0:日曜日, 1:月曜日, ...)
  return startDays[monthIndex];
}

function setCollectionInfo(sheet, startRow, calendarData, thursdayCounter, currentMonth) {
  var isFirstWeekOfJanuary = currentMonth === '1月';
  var firstWeekPassed = false;
  var wednesdayCounter = 0;
  
  for (var i = 0; i < calendarData.length; i++) {
    var hasDateInWeek = calendarData[i].some(date => date !== '');
    if (hasDateInWeek && isFirstWeekOfJanuary && !firstWeekPassed) {
      for (var j = 1; j < 6; j++) { // 月曜日から金曜日まで
        if (calendarData[i][j] !== '') {
          var cell = sheet.getRange(startRow + i, j + 1);
          var currentValue = cell.getValue();
          cell.setValue(currentValue + '\n収集なし');
        }
      }
      firstWeekPassed = true;
      continue;
    }
    
    for (var j = 1; j < 7; j++) {
      if (calendarData[i][j] === '') continue;
      
      var cell = sheet.getRange(startRow + i, j + 1);
      var currentValue = cell.getValue();
      
      switch(j) {
        case 1: // 月曜日：プラスチック類
          cell.setValue(currentValue + '\nプラスチック類');
          break;
        case 2: case 5: // 火曜日と金曜日：燃やせるゴミ
          cell.setValue(currentValue + '\n燃やせるゴミ');
          break;
        case 3: // 水曜日
          var wednesdayValue = getWednesdayValue(wednesdayCounter);
          cell.setValue(currentValue + '\n' + wednesdayValue);
          wednesdayCounter++;
          break;
        case 4: // 木曜日
          var thursdayValue = (thursdayCounter) % 2 === 0 ? '古紙類' : 'ビン、カン、ペットボトル';
          cell.setValue(currentValue + '\n' + thursdayValue);
          thursdayCounter++;
          break;
      }
    }
  }
}

function getWednesdayValue(counter) {
  if (counter === 0) return '衣類・布類';
  return counter % 2 === 1 ? '燃やせないゴミ' : '収集なし';
}

function getThursdayCount(calendarData) {
  return calendarData.reduce((count, week) => week[4] !== '' ? count + 1 : count, 0);
}