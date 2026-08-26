<?php
include("config.php");

if($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['username']) && isset($_POST['password'])) {
        $username = trim($_POST['username']);
        $password = hash('sha256', trim($_POST['password']));
        //Add secure sql query code between these two comments. DO NOT MODIFY THE CODE BEFORE THIS LINE
        //$sql = "SELECT username, password FROM loginusers WHERE username = '" . $username . "' AND password = '" . $password . "'"; // VULERABLE LINE OF CODE. You could exploit this by submitting ' OR 1=1; # as the username.
        //you may use the $conn variable here: ex: $stmt =  $conn->prepare(......... When you are preparing string arguments, you cannot use single quotes in the query.
        //Note: If you choose to use parameterized queries in your solution, you can fetch results of your SQL query by using something like $result = $stmt->fetch() after you execute the query.
        //Afterwards, you can see whether or not the query returned results by seeing whether !$result is false or not.
        // $result = $conn->query($sql);
        // $count = $result->num_rows;
        // if($count > 0) {
        //      header('Location: /success.php'); //login.php must redirect to /success.php for successful logins.
        // }
        // else {
        //      header('Location: /invalid.php'); //login.php must redirect to /invalid.php for failed logins.
        // }
        // my code

        
        $sql = "SELECT username, password FROM loginusers WHERE username = ? AND password = ?";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param('ss',$username, $password);
        // $stmt = $stmt->bind_Param(2, $password);
        $stmt->execute();
        $result = $stmt->fetch();
        // https://stackoverflow.com/questions/4286586/best-way-to-check-if-mysql-query-returned-any-results
        
        if (!$result == false) {
                header('Location: /success.php'); //login.php must redirect to /success.php for successful logins.
        }
        else {
                header('Location: /invalid.php'); //login.php must redirect to /invalid.php for failed logins.
        }




        //DO NOT MODIFY THE CODE BELOW THIS LINE
}
else {
        header('Location: /index.php');
}
?>





        
        //DO NOT MODIFY THE CODE BELOW THIS LINE
}
else {
        header('Location: /index.php');
}
?>
