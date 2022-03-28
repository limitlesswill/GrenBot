<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" 
content="width=device-width,
initial-scale=1.0">
<title>Form Sweet Form</title>
</head>
<body align ="center" style=
"color:black;background-color:white;">

<form method="post" autocomplete="off" 
align="center">

<table align="center">
<tr>  
<td>Title</td>
<td>
<input size="30" required
type="text" name="title" 
placeholder="Place your title here"/>
</td>
</tr>
<tr>
<td>Content</td>
<td> 
<textarea rows="3" cols="31"
required name="content" 
placeholder="place your content here">
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

<?php

if( isset($_POST['title']) )
{
$url = $_SERVER['DISCORD_WEBHOOK'];
$headers = 
[
'Content-Type: application/json; 
charset=utf-8' 
];

$POST = 
[ 
'username' => 'Guest', 
'content' => 
"<@333529891163340801>\r\n"
."             **".$_POST['title']."**\r\n"
.$_POST['content'] 
];

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($POST));
curl_exec($ch);

}
?>
