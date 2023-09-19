<?php
$conn=mysqli_connect('localhost','root','','nikhil_db')or die('connection failed');

if(isset($_POST['submit'])){
    $name=mysqli_real_escape_string($conn, $_POST['name']);
    $email=mysqli_real_escape_string($conn, $_POST['email']);
    $number=$_POST['number'];
    $date=$_POST['date'];

    $insert =mysqli_query($conn, "INSERT INTO `hospital`(name,email,number,date) VALUES ('$name','$email','$number','$date')") or die('query failed');

    if($insert){
        $message[]='appointment made successfully';
    }else{
        $message[]='appointment failed';
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Petzo Hospital</title>

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.3.0/css/all.min.css">

    <link rel="stylesheet" href="style.css">

    <script src="js/script.js"></script>
    

</head>
<body>

<header class="header">
           <a href="#" class="logo"> <i class="fas fa-heartbeat"></i> <strong>Nikhil</strong> medical</a>

           <nav class="navbar">
               <a href="#home">home</a>
               <a href="#about">about</a>
               <a href="#services">services</a>
               <a href="#doctors">doctors</a>
               <a href="#appointment">appointment</a>
               <a href="#review">review</a>
               <a href="#blogs">blogs</a>
           </nav>

           <div id="menu-btn" class="fas fa-bars"></div>

</header>

<section class="home" id="home">

    <div class="image">
        <img src="images/home.jpg" alt="">
    </div>

    <div class="content">
        <h3>we take care of your healthy life</h3>
        <p>A person who as physical health is likely to have bodily functions and processes working at their peak</p>
        <a href="appointment" class="btn"> appointment <span class="fas fa-chevron-right"></span></a>

    </div>

</section>

<section class="icons-container">
   
    <div class="icons">
       <i class="fas fa-user-md"></i>
        <h3>150+</h3>
        <p>doctors at work</p>
    </div>

    <div class="icons">
        <i class="fas fa-users"></i>
        <h3>1350+</h3>
        <p>satisfied patient</p>
    </div>

    <div class="icons">
        <i class="fas fa-procedures"></i>
        <h3>450+</h3>
        <p>bed facility</p>
    </div>

    <div class="icons">
        <i class="fas fa-hospital"></i>
        <h3>150+</h3>
        <p>available hospitals</p>
    </div>
    
</section>

<section class="about" id="about">

    <h1 class="heading"> <span>about</span> us</h1>

    <div class="row">

        <div class="image">
            <img src="images/about.jpg" alt="">
        </div>

        <div class="content">
            <h3>take the world's best quality treatment</h3>
            <p>Give yourself a new life everyone deserves a good and healthy life</p>
            <a href="#" class="btn">learn more<span class="fas fa-chevron-right"></span></a>
        </div>
    </div>

</section>

<section class="services" id="services">

    <h1 class="heading"> our <span>services</span> </h1>

    <div class="box-container">

        <div class="box">
            <i class="fas fa-notes-medical"></i>
            <h3>Free checkups</h3>
            <p>All services are provided with all our love and respect</p>
            <a href="#" class="btn"> learn more <span class="fas fa-chevron-right"></span></a>
        </div>

        <div class="box">
            <i class="fas fa-ambulance"></i>
            <h3>24/7 ambulance</h3>
            <p>All services are provided with all our love and respect</p>
            <a href="#" class="btn">learn more <span class="fas fa-chevron-right"></span></a>
        </div>

        <div class="box">
            <i class="fas fa-user-md"></i>
            <h3>Expert doctor</h3>
            <p>All services are provided with all our love and respect</p>
            <a href="#" class="btn">learn more <span class="fas fa-chevron-right"></span></a>
        </div>

        <div class="box">
            <i class="fas fa-heartbeat"></i>
            <h3>Total care</h3>
            <p>All services are provided with all our love and respect</p>
            <a href="#" class="btn">learn more <span class="fas fa-chevron-right"></span></a>
        </div>
        
    </div>
</section>

<section class="doctors" id="doctors">

    <h1 class="heading"> our <span>doctors</span></h1>

    <div class="box-container">

        <div class="box">
            <img src="images/doctor1.jpg" alt="">
            <h3>Nikhil</h3>
            <span>Expert doctor</span>
            <div class="share">
                <a href="#" class="fab fa-facebook-f"></a>
                <a href="#" class="fab fa-twitter"></a>
                <a href="#" class="fab fa-instagram"></a>
                <a href="#" class="fab fa-linkedin"></a>
            </div>
        </div>

        <div class="box">
            <img src="images/doctor2.jpg" alt="">
            <h3>Nikhil</h3>
            <span>Expert doctor</span>
            <div class="share">
                <a href="#" class="fab fa-facebook-f"></a>
                <a href="#" class="fab fa-twitter"></a>
                <a href="#" class="fab fa-instagram"></a>
                <a href="#" class="fab fa-linkedin"></a>
            </div>
        </div>

        <div class="box">
            <img src="images/doctor3.jpg" alt="">
            <h3>Nikhil</h3>
            <span>Expert doctor</span>
            <div class="share">
                <a href="#" class="fab fa-facebook-f"></a>
                <a href="#" class="fab fa-twitter"></a>
                <a href="#" class="fab fa-instagram"></a>
                <a href="#" class="fab fa-linkedin"></a>
            </div>
        </div>

        <div class="box">
            <img src="images/doctor4.jpg" alt="">
            <h3>Nikhil</h3>
            <span>Expert doctor</span>
            <div class="share">
                <a href="#" class="fab fa-facebook-f"></a>
                <a href="#" class="fab fa-twitter"></a>
                <a href="#" class="fab fa-instagram"></a>
                <a href="#" class="fab fa-linkedin"></a>
            </div>
        </div>

        <div class="box">
            <img src="images/doctor5.jpg" alt="">
            <h3>Nikhil</h3>
            <span>Expert doctor</span>
            <div class="share">
                <a href="#" class="fab fa-facebook-f"></a>
                <a href="#" class="fab fa-twitter"></a>
                <a href="#" class="fab fa-instagram"></a>
                <a href="#" class="fab fa-linkedin"></a>
            </div>
        </div>

        <div class="box">
            <img src="images/doctor6.jpg" alt="">
            <h3>Nikhil</h3>
            <span>Expert doctor</span>
            <div class="share">
                <a href="#" class="fab fa-facebook-f"></a>
                <a href="#" class="fab fa-twitter"></a>
                <a href="#" class="fab fa-instagram"></a>
                <a href="#" class="fab fa-linkedin"></a>
            </div>
        </div>

        <div class="box">
            <img src="images/doctor7.jpg" alt="">
            <h3>Nikhil</h3>
            <span>Expert doctor</span>
            <div class="share">
                <a href="#" class="fab fa-facebook-f"></a>
                <a href="#" class="fab fa-twitter"></a>
                <a href="#" class="fab fa-instagram"></a>
                <a href="#" class="fab fa-linkedin"></a>
            </div>
        </div>

        <div class="box">
            <img src="images/doctor8.jpg" alt="">
            <h3>Nikhil</h3>
            <span>Expert doctor</span>
            <div class="share">
                <a href="#" class="fab fa-facebook-f"></a>
                <a href="#" class="fab fa-twitter"></a>
                <a href="#" class="fab fa-instagram"></a>
                <a href="#" class="fab fa-linkedin"></a>
            </div>
        </div>

        <div class="box">
            <img src="images/doctor9.jpg" alt="">
            <h3>Nikhil</h3>
            <span>Expert doctor</span>
            <div class="share">
                <a href="#" class="fab fa-facebook-f"></a>
                <a href="#" class="fab fa-twitter"></a>
                <a href="#" class="fab fa-instagram"></a>
                <a href="#" class="fab fa-linkedin"></a>
            </div>
        </div>

    </div>
</section>

<section class="appointment" id="appointment">

    <h1 class="heading"> <span>appointment</span> Now </h1>

    <div class="row">

        <div class="image">
            <img src="images/appointment.jpg" alt="">
        </div>

        <form action="<?php echo $_SERVER['PHP_SELF'];?>" method="post">
        <?php
             if(isset($message)){
                foreach($message as $message) {
                    echo'<p class="message">'.$message.'</P>';
                }
            }

        ?>
            <h3>Make appointment</h3>
            <input type="text" name="name" placeholder="your name" class="box">
            <input type="number" name="number" placeholder="your number" class="box">
            <input type="email" name="email" placeholder="your email" class="box">
            <input type="date" name="date"  class="box">
            <input type="submit" name="submit" value="Appointment Now" class="btn">
        </form>
    </div>
</section>

<section class="review" id="review">

    <h1 class="heading"> client <span>review</span> </h1>

    <div class="box-container">

        <div class="box">
            <img src="images/review1.jpg" alt="">
            <h3>Nikhil</h3>
            <div class="stars">
                <i class="fas fa-star"></i>
                <i class="fas fa-star"></i>
                <i class="fas fa-star"></i>
                <i class="fas fa-star"></i>
                <i class="fas fa-star-half-alt"></i>
            </div>
            <p class="text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Nobis, possimus? Voluptatum quia perferendis ex impedit.</p>
        </div>

        <div class="box">
            <img src="images/review2.jpg" alt="">
            <h3>Nikhil</h3>
            <div class="stars">
                <i class="fas fa-star"></i>
                <i class="fas fa-star"></i>
                <i class="fas fa-star"></i>
                <i class="fas fa-star"></i>
                <i class="fas fa-star-half-alt"></i>
            </div>
            <p class="text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Nobis, possimus? Voluptatum quia perferendis ex impedit.</p>
        </div>

        <div class="box">
            <img src="images/review3.jpg" alt="">
            <h3>Nikhil</h3>
            <div class="stars">
                <i class="fas fa-star"></i>
                <i class="fas fa-star"></i>
                <i class="fas fa-star"></i>
                <i class="fas fa-star"></i>
                <i class="fas fa-star-half-alt"></i>
            </div>
            <p class="text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Nobis, possimus? Voluptatum quia perferendis ex impedit.</p>
        </div>

    </div>
</section>

<section class="blogs" id="blogs">

    <h1 class="heading"> Our <span>blogs</span> </h1>

    <div class="box-container">

        <div class="box">
            <div class="image">
                <img src="images/blog1.img" alt="">
            </div>
            <div class="content">
                <div class="icon">
                    <a href="#"> <i class="fas fa-calender"></i> 18 february,2023</a>
                    <a href="#"> <i class="fas fa-user"></i> by Nikhil</a>
                </div>
                <h3>blog title Nikhil goes here</h3>
                <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Libero voluptatem provident consequuntur harum ut. Illo incidunt quam velit, fugit quibusdam illum, omnis, dolores vel officiis corrupti minus quaerat a nulla.</p>
                <a href="#" class="btn"> learn more <span class="fas fa-chevron-right"></span> </a>
            </div>
        </div>

        <div class="box">
            <div class="image">
                <img src="images/blog2.img" alt="">
            </div>
            <div class="content">
                <div class="icon">
                    <a href="#"> <i class="fas fa-calender"></i> 18 february,2023</a>
                    <a href="#"> <i class="fas fa-user"></i> by Nikhil</a>
                </div>
                <h3>blog title Nikhil goes here</h3>
                <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Libero voluptatem provident consequuntur harum ut. Illo incidunt quam velit, fugit quibusdam illum, omnis, dolores vel officiis corrupti minus quaerat a nulla.</p>
                <a href="#" class="btn"> learn more <span class="fas fa-chevron-right"></span> </a>
            </div>
        </div>

        <div class="box">
            <div class="image">
                <img src="images/blog3.jpg" alt="">
            </div>
            <div class="content">
                <div class="icon">
                    <a href="#"> <i class="fas fa-calender"></i> 18 february,2023</a>
                    <a href="#"> <i class="fas fa-user"></i> by Nikhil</a>
                </div>
                <h3>blog title Nikhil goes here</h3>
                <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Libero voluptatem provident consequuntur harum ut. Illo incidunt quam velit, fugit quibusdam illum, omnis, dolores vel officiis corrupti minus quaerat a nulla.</p>
                <a href="#" class="btn"> learn more <span class="fas fa-chevron-right"></span> </a>
            </div>
        </div>

        <div class="box">
            <div class="image">
                <img src="images/blog4.img" alt="">
            </div>
            <div class="content">
                <div class="icon">
                    <a href="#"> <i class="fas fa-calender"></i> 18 february,2023</a>
                    <a href="#"> <i class="fas fa-user"></i> by Nikhil</a>
                </div>
                <h3>blog title Nikhil goes here</h3>
                <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Libero voluptatem provident consequuntur harum ut. Illo incidunt quam velit, fugit quibusdam illum, omnis, dolores vel officiis corrupti minus quaerat a nulla.</p>
                <a href="#" class="btn"> learn more <span class="fas fa-chevron-right"></span> </a>
            </div>
        </div>

        <div class="box">
            <div class="image">
                <img src="images/blog5.img" alt="">
            </div>
            <div class="content">
                <div class="icon">
                    <a href="#"> <i class="fas fa-calender"></i> 18 february,2023</a>
                    <a href="#"> <i class="fas fa-user"></i> by Nikhil</a>
                </div>
                <h3>blog title Nikhil goes here</h3>
                <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Libero voluptatem provident consequuntur harum ut. Illo incidunt quam velit, fugit quibusdam illum, omnis, dolores vel officiis corrupti minus quaerat a nulla.</p>
                <a href="#" class="btn"> learn more <span class="fas fa-chevron-right"></span> </a>
            </div>
        </div>

        <div class="box">
            <div class="image">
                <img src="images/blog6.img" alt="">
            </div>
            <div class="content">
                <div class="icon">
                    <a href="#"> <i class="fas fa-calender"></i> 18 february,2023</a>
                    <a href="#"> <i class="fas fa-user"></i> by Nikhil</a>
                </div>
                <h3>blog title Nikhil goes here</h3>
                <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Libero voluptatem provident consequuntur harum ut. Illo incidunt quam velit, fugit quibusdam illum, omnis, dolores vel officiis corrupti minus quaerat a nulla.</p>
                <a href="#" class="btn"> learn more <span class="fas fa-chevron-right"></span> </a>
            </div>
        </div>
    </div>
</section>

<section class="footer">

    <div class="box-container">

        <div class="box">
            <h3>quick links</h3>
            <a href="#"> <i class="fas fa-chevron-right"></i> home </a>
            <a href="#"> <i class="fas fa-chevron-right"></i> about </a>
            <a href="#"> <i class="fas fa-chevron-right"></i> services </a>
            <a href="#"> <i class="fas fa-chevron-right"></i> doctors </a>
            <a href="#"> <i class="fas fa-chevron-right"></i> appointment </a>
            <a href="#"> <i class="fas fa-chevron-right"></i> review </a>
            <a href="#"> <i class="fas fa-chevron-right"></i> blogs </a>
        </div>

        <div class="box">
            <h3>Our services</h3>
            <a href="#"> <i class="fas fa-chevron-right"></i> dental care </a>
            <a href="#"> <i class="fas fa-chevron-right"></i> message therapy </a>
            <a href="#"> <i class="fas fa-chevron-right"></i> cardioloty </a>
            <a href="#"> <i class="fas fa-chevron-right"></i> diagnosis </a>
            <a href="#"> <i class="fas fa-chevron-right"></i> ambulance service </a>
            
        </div>

        <div class="box">
            <h3>appointment info</h3>
            <a href="#"> <i class="fas fa-phone"></i> +4764959354 </a>
            <a href="#"> <i class="fas fa-phone"></i> +5455478488 </a>
            <a href="#"> <i class="fas fa-envelope"></i> nikhil4@gmail.com </a>
            <a href="#"> <i class="fas fa-envelope"></i> tiger13@gmail.com </a>
            <a href="#"> <i class="fas fa-map-market-alt"></i> chennai,TamilNadu </a>
            
        </div>

        <div class="box">
            <h3>follow us</h3>
            <a href="#"> <i class="fab fa-faceappointment-f"></i> faceappointment </a>
            <a href="#"> <i class="fab fa-twitter"></i> twiiter </a>
            <a href="#"> <i class="fab fa-instagram"></i> instagram </a>
            <a href="#"> <i class="fab fa-linkedin"></i> linkedin </a>
            <a href="#"> <i class="fab fa-pinterest"></i> pinterest </a>

        </div>
    </div>

    <div class="credit"> created by <span> Nikhil</span> | all rights reserved </div>
</section>

</body>
</html>