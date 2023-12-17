<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add data</title>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
</head>

<body>
    <div class="container">
        <div class="h4 text-center alert alert-primary mb-2 mt-4" role="alert">Add data</div>
        <form method="POST" action="insert.php">
            <label>FirstName</label>
            <input type="text" name="fname" class="form-control" placeholder="ชื่อ" required><br>
            <label>LastName</label>
            <input type="text" name="lname" class="form-control" placeholder="นามสุล" required><br>
            <label>Phone</label>
            <input type="text" name="telephone" class="form-control" placeholder="เบอร์โทร" maxlength="10" required><br>
            <input type="submit" value="Submit" class="btn btn-success">
            <a href="index.php" class="btn btn-danger">Cancel</a>
        </form>
    </div>
</body>

</html>