<?php
$title = "";
$content = "";

function sen()
{
$message = "LOOOOOL";
echo "uuuuuuuuuuuuuuu";
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
action="form.php" onsubmit = "sen()">

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
onclick="sen()"/>

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

<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>hhhhhh</title>
</head>
<body>
<pre>
This is a test 
<script type="text/javascript">
alert("hello there");
<script>
<pre>
</body>
</html>
