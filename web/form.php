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
</html>
';


/*
if( isset($_POST['title']) )
{
$url = $_SERVER['WEBHOOK'];
$headers = 
[
'Content-Type: application/json; charset=utf-8' 
];

$POST = 
[ 
'username' => 'Guest', 
'content' => 
"title is: 
             **".$_POST['title']."**\r\n"
.$_POST['content'] 
];

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, 
$headers);
curl_setopt($ch, CURLOPT_POSTFIELDS, 
json_encode($POST));
curl_exec($ch);
}
*/
if (isset($_GET['hub_mode']) && isset($_GET['hub_challenge']) && isset($_GET['hub_verify_token']))
{
echo $_GET['hub_challenge'];
}else if(isset($_POST['value']['post_id']))
{
$url = 'https://graph.facebook.com/'.$_SERVER['fb_page_id'].'_'.$_POST['value']['post_id'].'/comments';
$headers = 
[
'Content-Type: application/json; charset=utf-8' 
];

$POST = 
[ 
'access_token' => $_SERVER['fb_token'], 
'message' => $_POST['value']['message']
];

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, 
$headers);
curl_setopt($ch, CURLOPT_POSTFIELDS, 
json_encode($POST));
curl_exec($ch);
}else{
echo $html;
}
?>
