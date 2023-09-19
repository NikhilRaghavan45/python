let menuBar=document.querySelector('.menubox');
let navbar=document.querySelector('.navbar');

menuBar.onclick = () =>{
    menuBar.classList.toggle('bx-x');
    navbar.classList.toggle('active');
}; 