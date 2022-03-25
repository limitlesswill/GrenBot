<?php 
/*include_once("home.html");*/
echo "<h1>HELLO THERE</h1><br/>"
.$_SERVER["REMOTE_HOST"]
."<br/>
<h1>You're viewing this page throught "
.$_SERVER["REMOTE_ADDR"].":"
.$_SERVER["REMOTE_PORT"]."</h1>
<br/>More information:\n";

foreach($_SERVER as $key => $val) 
echo $key."[".$val."]<br/>";

print_r($_POST);
echo "<br/>";
print_r($_GET);
echo "<br/>";
print_r($_FILES);
?>
