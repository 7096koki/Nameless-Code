function ToroMail() {
 const pokepiList = {
   "トロ": "ニャ",
   "トロ": "ニャ",
   "トロ": "ニャ",
   "トロ": "ニャ",
   "トロ": "ニャ",
   "クロ": "みャ",
   "ソラ": "じャ",
   "ジュン": "ピョン",
   "ピエール": "わン",
   "スズキ": "ロボ"
 };


 const pokepiKeys = Object.keys(pokepiList);
 const pokepiNumber = Math.floor(Math.random() * pokepiKeys.length);
 const name = pokepiKeys[pokepiNumber];
 const lt = pokepiList[name];


 let mailText = [];
 mailText.push(`こんにちは、${name} ${lt}！今日は`);




 const food = [
   "かき氷",
   "お寿司",
   "もやし",
   "ラーメン",
   "カツ丼",
   "ハンバーグ",
   "アイスクリーム"
 ];


 const food_kansou = [
   "ちょっとだけおいしかった",
   "すっごいおいしかった",
   "まあまあおいしかった"
 ];


 const foodKeys = Object.keys(food);
 const foodValues = Object.values(food);
 const picup = Math.floor(Math.random() * foodKeys.length);


 const template = [`${food[picup]}を食べた${lt}。\n気になるお味は...?${food_kansou[Math.floor(Math.random() * food_kansou.length)]}${lt}`
 ];


 mailText.push(template[0]);


 return mailText.join("");
}


function sendToroMailDaily() {
 const recipientEmail = "kokiando96@gmail.com"; // ★ あなたのメールアドレスに変更してください
 const subject = "今日のポケピのつぶやき";
 const body = ToroMail();


 GmailApp.sendEmail(recipientEmail, subject, body);
}


sendToroMailDaily()


function setupDailyTrigger() {
 // 既存のトリガーを削除 (重複を防ぐため)
 const triggers = ScriptApp.getProjectTriggers();
 for (const trigger of triggers) {
   if (trigger.getHandlerFunction() === "sendToroMailDaily") {
     ScriptApp.deleteTrigger(trigger);
   }
 }


ScriptApp.newTrigger("sendToroMailDaily")


 // 毎日正午に sendToroMailDaily 関数を実行するトリガーを作成
 ScriptApp.newTrigger("sendToroMailDaily")
   .timeBased()
   .atHour(12)
   .everyDays(1)
   .create();
}
