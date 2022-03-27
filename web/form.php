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

<form method="get" autocomplete="off"
align="center">

<table align="center">
<tr>
<td>Title</td>
<td>      
<input size="30"
type="text" name="title"
placeholder="Place your title here">
</td>
</tr>
<tr>
<td>Content</td>
<td>     
<input size="45"
type="textarea" name="content"
placeholder="place your content here">
</td>
</tr> 
</table>

</form>

<br/><br/>

<a href="index.php"
style="text-decoration:none;">
Go Home</a>
</body>
</html>

<?php
if( isset($_GET['title']) )
{
     echo "<br/><br/>".$_GET['title'];
}
?>
