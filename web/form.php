<?php
$title = "";
$content = "";

function sen()
{
$message = "LOOOOOL";
echo "alert(\"Alert on this page thanks\");";
}

$html = '
<!DOCTYPE HTML>
<html lang="en">
<meta charset="UTF-8">
<head>
<title>Form Sweet Form</title>
</head>

<body align ="center" style=
"color:black;background-color:white;">

<form autocomplete="off"
align="center" method="POST"
action="form.php" onsubmit = "<?php sen();?>">

<table align="center">
<tr>
<td>Title</td>
<td>      
<input size="25"
type="text" name="title" id="tit"
placeholder="Place your title here">
</td>
</tr>
<tr>
<td>Content</td>
<td>     
<input size="25"
type="text" name="content" id="con"
placeholder="place your content here">
</td>
</tr> 
</table>
<input type="button" value="Submit" 
onclick="<?php sen();?>"/>

</form>
<br/><br/>
<a href="index.php"
style="text-decoration:none;">
Go Home</a>
</body>
</html>
';


echo $html;

?>
