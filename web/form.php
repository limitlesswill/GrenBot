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

if (isset($_GET['hub_mode']) && isset($_GET['hub_challenge']) && isset($_GET['hub_verify_token']))
{
echo $_GET['hub_challenge'];
}else if(isset($_POST['value']['post_id']))
{
$url = $_SERVER['DISCORD_WEBHOOK'];

$headers = 
[
'Content-Type: application/json; charset=utf-8' 
];

$POST = 
[ 
'username' => 'Facebook',
'avatar_url' => 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdps7VEksKG_PuqBOPS6CQ_vgojaRYxQbj3A&usqp=CAU',
'content' => file_get_contents('php://input')
];

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, 
$headers);
curl_setopt($ch, CURLOPT_POSTFIELDS, 
json_encode($POST));
curl_exec($ch);
echo 200;
}else{
echo $html;
}
?>
