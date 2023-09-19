<?php
$conn=mysqli_connect('localhost','root','','signin_db') or die('connection failed');

if(isset($_POST['submit'])){
  $name=mysqli_real_escape_string($conn,$_POST['name']);
  $number=$_POST['number'];
  $email=mysqli_real_escape_string($conn,$_POST['email']);
  $address=mysqli_real_escape_string($conn,$_POST['address']);

  $insert =mysqli_query($conn, "INSERT INTO `delivery`(name,number,email,address) VALUES ('$name','$number','$email','$address')") or die('query failed');

  if($insert){
      $message[]='signin made successfully';
  }else{
      $message[]='signin failed';
  }
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

   

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="style.css">
</head>
<body>
     
    <nav class="navbar navbar-expand-lg navbar-dark" id="navbar">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">PETZO FOODS</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarCollapse">
            <ul class="navbar-nav me-auto">
              <li class="nav-item">
                <a class="nav-link"  href="#home">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#about">about</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#product">product</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#contact">contact</a>
              </li>
            </ul>
            <button class="btn pd-3 my-4"><a class="nav-link" href="#formin"</a>Sign In</button>
         </div>
        </div>
      </nav>

      <section id="home">
        <h1 class="text-center">PETZO FOODS</h1>
      </section>

      <section id="about">
        <div class="container-fluid">
          <div class="row">
            <div class="col-lg-6 col-md-6 col-12">
                 <img src="css/about.jpg" class="img-fluid">
            </div>
            <div class="col-lg-6 col-md-6 col-12">
                <h1>ABOUT US</h1>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Cumque magni totam assumenda, dignissimos veritatis unde expedita ut laborum quisquam quos exercitationem, facere repellat maxime tempore debitis explicabo quam fugiat possimus.Lorem ipsum dolor sit amet consectetur adipisicing elit. Cumque magni totam assumenda, dignissimos veritatis unde expedita ut laborum quisquam quos exercitationem, facere repellat maxime tempore debitis explicabo quam fugiat possimus.Lorem ipsum dolor sit amet consectetur adipisicing elit. Cumque magni totam assumenda, dignissimos veritatis unde expedita ut laborum quisquam quos exercitationem, facere repellat maxime tempore debitis explicabo quam fugiat possimus.Lorem ipsum dolor sit amet consectetur adipisicing elit. Cumque magni totam assumenda, dignissimos veritatis unde expedita ut laborum quisquam quos exercitationem, facere repellat maxime tempore debitis explicabo quam fugiat possimus.Lorem ipsum dolor sit amet consectetur adipisicing elit. Cumque magni totam assumenda, dignissimos veritatis unde expedita ut laborum quisquam quos exercitationem, facere repellat maxime tempore debitis explicabo quam fugiat possimus.</p>
          </div>
        </div>
      </section>

      <section id="product">
          <div class="container m-5">
            <h1 class="text-center my-5">OUR PRODUCTS</h1>
            <div class="row">
              <div class="col-lg-4 col-md-4 col-12">
                <div class="card">
                  <img src="css/p.png" class="card-img-top">
                  <div class="card-body text-center">
                    <h5 class="card-title">Parotta</h5>
                    <a href="#" class="btn signin">Add to cart</a>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-4 col-12">
                <div class="card">
                  <img src="css/p1.png" class="card-img-top">
                  <div class="card-body text-center">
                    <h5 class="card-title">Idli</h5>
                    <a href="#" class="btn signin">Add to cart</a>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-4 col-12">
                <div class="card">
                  <img src="css/p2.png" class="card-img-top">
                  <div class="card-body text-center">
                    <h5 class="card-title">Poori</h5>
                    <a href="#" class="btn signin">Add to cart</a>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-4 col-12">
                <div class="card">
                  <img src="css/p3.png" class="card-img-top">
                  <div class="card-body text-center">
                    <h5 class="card-title">Dosa</h5>
                    <a href="#" class="btn signin">Add to cart</a>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-4 col-12">
                <div class="card">
                  <img src="css/p20.png" class="card-img-top">
                  <div class="card-body text-center">
                    <h5 class="card-title">Pizza</h5>
                    <a href="#" class="btn signin">Add to cart</a>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-4 col-12">
                <div class="card">
                  <img src="css/p5.png" class="card-img-top">
                  <div class="card-body text-center">
                    <h5 class="card-title">Burger</h5>
                    <a href="#" class="btn signin">Add to cart</a>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-4 col-12">
                <div class="card">
                  <img src="css/p70.png" class="card-img-top">
                  <div class="card-body text-center">
                    <h5 class="card-title">Chicken briyani</h5>
                    <a href="#" class="btn signin">Add to cart</a>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-4 col-12">
                <div class="card">
                  <img src="css/p7.png" class="card-img-top">
                  <div class="card-body text-center">
                    <h5 class="card-title">Chicken rice</h5>
                    <a href="#" class="btn signin">Add to cart</a>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-4 col-12">
                <div class="card">
                  <img src="css/p80.png" class="card-img-top">
                  <div class="card-body text-center">
                    <h5 class="card-title">Chicken noodles</h5>
                    <a href="#" class="btn signin">Add to cart</a>
                  </div>
                </div>
              </div>

              
            </div>          
      </section>

      <section id="contact">
          <div class="container box">
            <div class="row">
              <div class="col-lg-6 col-md-6 col-12">
                <img src="css/pg.png" class="img-fluid">
              </div>
              <div class="col-lg-6 col-md-6 col-12">
                <h1>CONTACT US</h1>
                <form class="mb-3">
                  <input type="text" class="form-control" placeholder="enter your name">
                  <input type="email" class="form-control" placeholder="enter your email">
                  <textarea class="form-control" placeholder="enter your message"></textarea>
                  <button class="btn signin">send</button>
                </form>
              </div>
            </div>
          </div>

      </section>

<section id="formin">
        
<div class="container">
  <form action="<?php echo $_SERVER['PHP_SELF'];?>" method="post">
  <?php
       if(isset($message)){
          foreach($message as $message) {
          echo'<p class="message">'.$message.'</P>';
       }
       }

  ?>
  <div class="row">
    <div class="col-25">
      <label for="name">name</label>
    </div>
    <div class="col-75">
      <input type="text" id="name" name="name" placeholder="Your name..">
    </div>
  </div>
  <div class="row">
    <div class="col-25">
      <label for="number">number</label>
    </div>
    <div class="col-75">
      <input type="text" id="number" name="number" placeholder="Your number..">
    </div>
  </div>
  <div class="row">
    <div class="col-25">
      <label for="email">email</label>
    </div>
    <div class="col-75">
      <input type="text" id="email" name="email" placeholder="Your email..">
    </div>
  </div>
  <div class="row">
    <div class="col-25">
      <label for="address">address</label>
    </div>
    <div class="col-75">
      <textarea id="address" name="address" placeholder="Write your address.." style="height:200px"></textarea>
    </div>
  </div>
  <br>
  <div class="row">
    <input type="submit" name="submit" value="Submit">
  </div>
  </form>
</div>
    
</section>

      <footer class="text-center">copyrights@Petzo foods</footer>

     
        


    
</body>
</html>
    