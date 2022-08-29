<?php

$html = '<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" 
content="width=device-width,
initial-scale=1.0">
<title>Form Sweet Form</title>
</head>
<body align ="center" style=
"color:black;background-color:white;">

<form method="get" autocomplete="off" 
align="center">

<table align="center">
<tr>  
<td>Mode</td>
<td>
<input size="30" required
type="text" name="hub_mode" maxlength="99" 
placeholder="It\'s always subscribe"/>
</td>
</tr>
<tr>
<td>Challenge</td>
<td>
<input size="30" required
type="text" name="hub_challenge"
maxlength="99" placeholder="Place an integer here"/>
</td>
</tr>
<tr>
<td>Verify Token</td>
<td> 
<textarea rows="3" cols="31"
required name="hub_verify_token" maxlength ="1900" 
placeholder="Place the access token here">
</textarea>
</td>
</tr> 
</table>
<br/>
<input type="submit" value="Submit"/>
</form>

<br/><br/>
<a href="index.php"
style="text-decoration:none;">
Go Home</a>
</body>
</html>';

function sendit($url,$payload)
{
$headers = 
[
'Content-Type: application/json; charset=utf-8' 
];
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, 
$headers);
curl_setopt($ch, CURLOPT_POSTFIELDS, 
json_encode($payload));
return curl_exec($ch);
}

if(isset($_GET['hub_mode']) && isset($_GET['hub_challenge']) && isset($_GET['hub_verify_token']))
{
echo $_GET['hub_challenge'];
}else if($_SERVER['REQUEST_METHOD'] === 'POST')
{
$data = json_decode(file_get_contents('php://input'), true);
if(($data['entry'][0]['changes'][0]['value']['from']['id'] != $_SERVER['fb_page_id']) && $data['entry'][0]['changes'][0]['value']['item'] == 'comment')
{
$scope_id = $data['entry'][0]['changes'][0]['value']['from']['id'];
$name = $data['entry'][0]['changes'][0]['value']['from']['name'];
$comment_id = $data['entry'][0]['changes'][0]['value']['comment_id'];
$msg = $data['entry'][0]['changes'][0]['value']['message'];
$url = 'https://graph.facebook.com/v14.0/';
$token_payload = ['access_token' => $_SERVER['fb_token']];
$comment_payload = ['message' => '@['.$scope_id.']'.chr(10).'تم التواصل على الخاص 💌'];
$private_reply_payload =
[
"recipient" => ["comment_id" => $comment_id],
"message" => ["attachment" =>
["type" => "template",
"payload" =>
["template_type" => "button",
"text" => ".أهلاً وسهلاً بحضرتك يا فندم",

"buttons" => [["type" => "postback","title" => "Dad jokes","payload" => "dad_jokes"],
["type" => "postback","title" => "Chuck Norris jokes","payload" => "chuck_jokes"],
["type" => "postback","title" => "Page Images","payload" => "imgs"]]

]]]];

sendit($url.$comment_id.'/likes',$token_payload);
sendit($url.$comment_id.'/comments',$comment_payload+$token_payload);
sendit($url.'me/messages',$private_reply_payload+$token_payload);
} else if(!empty($data['entry'][0]['messaging'][0]['postback']['payload']))
{
$token_payload = ['access_token' => $_SERVER['fb_token']];
$url = 'https://graph.facebook.com/v14.0/';
$sender_scope_id = $data['entry'][0]['messaging'][0]['sender']['id'];
$choice = $data['entry'][0]['messaging'][0]['postback']['payload'];
$msg = "";
switch($choice)
{
case "dad_jokes":
$msg = "You pressed Dad jokes";
break;
case "chuck_jokes":
$msg = "You pressed Chuck Norris jokes";
break;
case "imgs":
$msg = "You pressed Page Images";
break;
}
$msg_payload = ['recipient' => ['id' => $sender_scope_id],'message' => ['text' => $msg] ];
sendit($url.'/conversations',$msg_payload+$token_payload);
}

$dc = $_SERVER['DISCORD_WEBHOOK'];
$dc_payload = 
[ 
'username' => 'Facebook',
'avatar_url' => 'https://scontent.fcai1-3.fna.fbcdn.net/v/t39.8562-6/109960336_274477960450922_1306319190754819753_n.png?_nc_cat=107&ccb=1-7&_nc_sid=6825c5&_nc_eui2=AeEW0Tv6csstYDgEbtnMu-g4JxDCgWesWeInEMKBZ6xZ4jN15myTe-sJn1pUwiWyt2YnTf0E3QM3nWkTaegX1JNZ&_nc_ohc=creb8yK0R18AX-xUJZ5&_nc_ht=scontent.fcai1-3.fna&oh=00_AT8xmtU5v_S4xoW_zAaW9OWXh3wjta-Qk79nNkCqbXb_ow&oe=630A31B0',
'content' => var_export($data,true)
];
sendit($dc,$dc_payload);
echo 200;
}else{
echo $html;
}
?>
