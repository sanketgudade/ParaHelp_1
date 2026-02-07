<?php
$servername = "localhost";
$username = "root";
$password = "rajkumar@123@";
$dbname = "parahelp101";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $fullname = $_POST['fullname'];
    $user = $_POST['username'];
    $pass = password_hash($_POST['password'], PASSWORD_DEFAULT);  // Hashing the password

    // Check if username already exists
    $checkUser = $conn->prepare("SELECT * FROM users WHERE username = ?");
    $checkUser->bind_param("s", $user);
    $checkUser->execute();
    $result = $checkUser->get_result();

    if ($result->num_rows > 0) {
        echo "<script>alert('Username already exists. Please choose another one.'); window.location.href='signup.html';</script>";
    } else {
        // Insert new user
        $stmt = $conn->prepare("INSERT INTO users (fullname, username, password) VALUES (?, ?, ?)");
        $stmt->bind_param("sss", $fullname, $user, $pass);

        if ($stmt->execute()) {
            echo "<script>alert('Registration successful!'); window.location.href='login.html';</script>";
        } else {
            echo "Error: " . $stmt->error;
        }
    }
    $stmt->close();
}
$conn->close();
?>
