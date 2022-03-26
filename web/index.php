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
."\n".$_SERVER["HTTP_SEC_CH_UA_MOBILE"]
."\n".$_SERVER["HTTP_SEC_CH_UA"]
."\n".$_SERVER["HTTP_USER_AGENT"]
."\n".$_SERVER["HTTP_X_FORWARDED_PROTO"]
."\n".$_SERVER["HTTP_X_FORWARDED_FOR"]
.":".$_SERVER["HTTP_X_FORWARDED_PORT"];

foreach($_POST as $key => $val) 
echo $key."(".$val.")<br/>";

foreach($_GET as $key => $val) 
echo $key."{".$val."}<br/>";

foreach($_FILES as $key => $val) 
echo $key."[".$val."]<br/>";

echo '<a href="form.php">Go to The form</a>';

?>
