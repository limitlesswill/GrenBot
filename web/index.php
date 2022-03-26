<?php 
/*include_once("home.html");*/
echo "<h1>HELLO THERE</h1><br/>"
.$_SERVER["REMOTE_HOST"]
."<br/>
<h1>You're viewing this page throught "
.$_SERVER["REMOTE_ADDR"].":"
.$_SERVER["REMOTE_PORT"]."</h1>
<br/>More information:\n";

echo $_SERVER["HTTP_SEC_CH_UA_PLATFORM"]
."<br/>".$_SERVER["HTTP_SEC_CH_UA_MOBILE"]
."<br/>".$_SERVER["HTTP_SEC_CH_UA"]
."<br/>".$_SERVER["HTTP_USER_AGENT"]
."<br/>".$_SERVER["HTTP_X_FORWARDED_PROTO"]
."<br/>".$_SERVER["HTTP_X_FORWARDED_FOR"]
.":".$_SERVER["HTTP_X_FORWARDED_PORT"];

$post = "";
foreach($_POST as $key => $val) 
post.$key."(".$val.")<br/>";
echo $post."<br/>";

$get = "";
foreach($_GET as $key => $val) 
get.$key."{".$val."}<br/>";
echo $get."<br/>";

$files = "";
foreach($_FILES as $key => $val) 
files.$key."[".$val."]<br/>";
echo $files."<br/>";

$html = '
<!DOCTYPE html>
<head>
<title>Home Sweet Home</title>
</head>
<body>
<a href="form.php"
style="text-decoration:none;">
Go to The form</a>
</body>
</html>
';

echo ."<br/><br/><br/>".$html;

?>
