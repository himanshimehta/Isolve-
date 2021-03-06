from flask import Flask, redirect, url_for, request, render_template
import model1
from string import Template
import SI
import subprocess
import re
import base64

si_page = Template("""
  <html class="gr__" lang="en">
   <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      <meta name="description" content="Solve all your problems!">
      <meta name="author" content="Siddhartha Khanooja">
      <title>Dilton - A Math Word Problem Solver</title>
      <!-- Bootstrap core CSS -->
      <link href= "/static/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
      <!-- Custom fonts for this template -->
      <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">
      <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
      <link href="https://fonts.googleapis.com/css?family=Kaushan+Script" rel="stylesheet" type="text/css">
      <link href="https://fonts.googleapis.com/css?family=Droid+Serif:400,700,400italic,700italic" rel="stylesheet" type="text/css">
      <link href="https://fonts.googleapis.com/css?family=Roboto+Slab:400,100,300,700" rel="stylesheet" type="text/css">
      <script src="https://code.jquery.com/jquery-3.2.1.min.js">
      </script>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.min.css">
      <!-- Custom styles for this template -->
      <link href= "/static/css/agency.min.css" rel="stylesheet">
      <script type="text/javascript">
         $$(document).on('click', '.table > tbody > tr', function(e){
               e.preventDefault();
               var text = $$(this).text();
               var trimmedtext = $$.trim(text);
               $$('.form-control').val(trimmedtext);
               }); 
         $$(document).on('click','#si', function(e){
               e.preventDefault();
               $$(".replace").replaceWith('<div class="replace"> <div class="row" id="siexamples"> <div class="text-center col-lg-12"> <table class="table table-bordered table-hover"> <thead> <tr id="tableheader"> <th class="text-center">Simple Interest Examples</th> </tr> </thead> <tbody> <tr id="example1" style="height:80px;overflow:hidden;cursor:pointer"> <td>What sum of money will earn an interest of $$162 in 3 years at the rate of 12% per annum?</td> </tr> <tr id="example2" style="height:80px;overflow:hidden;cursor:pointer"> <td>How much time will it take for an amount of $$900 to yield $$81 as interest at 4.5% per annum of simple interest?</td> </tr> <tr id="example3" style="height:80px;overflow:hidden;cursor:pointer"> <td>A sum fetched a total simple interest of $$929.20 at the rate of 8% per annum in 5 years. What is the sum?</td> </tr> <tr id="example4" style="height:80px;overflow:hidden;cursor:pointer"> <td>$$10,000 is invested at 5% interest rate in 1 year. Find the interest.</td> </tr> <tr id="example5" style="height:80px;overflow:hidden;cursor:pointer"> <td>$$3,500 is given at 7% p.a. rate of interest. Find the interest which will be received at the end of one year.</td> </tr> <tr id="example6" style="height:80px;overflow:hidden;cursor:pointer"> <td>If Manohar pays an interest of $$750 for 2 years on a sum of $$4,500, find the rate of interest.</td> </tr> </tbody> </table> </div> </div> </div>');
               $$("#unique").attr("action","http://127.0.0.1:5000/sipred");
               $$("#buttontext").text("Simple Interest");
         });
         $$(document).on('click','#op', function(e){
               e.preventDefault();
               $$(".replace").replaceWith('<div class="replace"> <div class="row" id="opexamples"> <div class="text-center col-lg-12"> <table class="table table-bordered table-hover"> <thead> <tr id="tableheader"> <th class="text-center">Operation Prediction Examples</th> </tr> </thead> <tbody> <tr id="example1" style="height:80px;overflow:hidden;cursor:pointer"> <td>Joan found 70 seashells on the beach. She gave Sam some of her seashells. She now has 27 seashells. How many seashells did she give to Sam?</td> </tr> <tr id="example2" style="height:80px;overflow:hidden;cursor:pointer"> <td>There were 28 bales of hay in the barn. Tim stacked some bales in the barn today. There are now 54 bales of hay in the barn. How many bales did he store in the barn?</td> </tr> <tr id="example3" style="height:80px;overflow:hidden;cursor:pointer"> <td>Mary is baking a cake. The recipe wants 8 cups of flour. She already put in 2 cups. How many cups does she need to add?</td> </tr> <tr id="example4" style="height:80px;overflow:hidden;cursor:pointer"> <td> Michelle played 12 basketball games this year. They were defeated during 4 games. How many games did they win?</td> </tr> <tr id="example5" style="height:80px;overflow:hidden;cursor:pointer"> <td>John is having $$5. Manohar gives to him $$7 more. How much does he have now?</td> </tr> <tr id="example6" style="height:80px;overflow:hidden;cursor:pointer"> <td>Sam had 6 apples. He gave 3 apples to Fred. How many apples does Sam have now?</td> </tr> </tbody> </table> </div> </div> </div>');
               $$("#unique").attr("action","http://127.0.0.1:5000/oppred");
               $$("#buttontext").text("Operation Prediction");

         });

      </script>
      <style>
         .table {
           border: 0.5px solid #000000;
         }
         .table-bordered > thead > tr > th,
         .table-bordered > tbody > tr > th,
         .table-bordered > tfoot > tr > th,
         .table-bordered > thead > tr > td,
         .table-bordered > tbody > tr > td,
         .table-bordered > tfoot > tr > td {
            border: 0.5px solid #000000;
         }
         .bg-primary, .dropdown-toggle, .rightb {
            background-color: #f05f40 !important;
         }
         a {
            color : black;
         }
         
         #start {
            padding: 50px 0;
         }

         #about, #team {
            padding: 75px 0;
         }

         #motivation {
            padding: 100px 0;
         }
         #motihead {
            margin-bottom: 50px;
         }
      </style>
   </head>
   <body id="page-top" data-gr-c-s-loaded="true" class="">
      <!-- Navigation -->
      <nav class="navbar navbar-expand-lg navbar-dark fixed-top" id="mainNav">
         <div class="container">
            <a class="navbar-brand js-scroll-trigger" href="#page-top">Dilton - The Math Word Problem Solver</a>
            <button class="navbar-toggler navbar-toggler-right collapsed" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
            Menu
            <i class="fa fa-bars"></i>
            </button>
            <div class="collapse navbar-collapse" id="navbarResponsive">
               <ul class="navbar-nav text-uppercase ml-auto">
                  <li class="nav-item">
                     <a class="nav-link js-scroll-trigger" href="#start">Start</a>
                  </li>
                  <li class="nav-item">
                     <a class="nav-link js-scroll-trigger" href="#motivation">Motivation</a>
                  </li>
                  <li class="nav-item">
                     <a class="nav-link js-scroll-trigger" href="#contact">Contact</a>
                  </li>
               </ul>
            </div>
         </div>
      </nav>
      <!-- Header -->
      <header class="masthead">
         <div class="container">
         </div>
      </header>
      <br><br><br><br><br><br>
      <img src="/static/img/omega.png" class="rounded mx-auto d-block"/>
      <!-- Input Box -->
      <section id="start">
         <div class="container">
            <div class="row">
               <div class="col-lg-12 text-center">
                  <h2 class="section-heading text-uppercase">Dilton</h2>
               </div>
            </div>
            <form action="http://127.0.0.1:5000/oppred" method="post" id="unique">
            <div class="row">
               <div class="col-lg-12">
                   <div class="input-group">
                     <div class="input-group-btn">
                       <button type="button" class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" id="buttontext">
                         Type of Question
                       </button>
                       <div class="dropdown-menu">
                         <a class="dropdown-item" href="#" id="si">Simple Interest</a>
                         <a class="dropdown-item" href="#" id="op">Operation Prediction</a>
                       </div>
                     </div>
                        <input type="text" class="form-control" aria-label="Text input with dropdown button" placeholder="Enter your question. " autocomplete="off" name="qtest">
                        <span class="input-group-btn">
                            <input type="submit"class="btn btn-secondary rightb" type="button" value="Solve!"></button>
                        </span>
                   </div>
                 </div>
              </div>
              </form>
              <div class="row">
               <div class="col-lg-8 mx-auto text-center">
                  <p>The question is: </p>
                  <p> "${name}" </p>
                  <p class="large">The answer is: </p>
                  <p> ${siunknown}  ${sianswer}.</p>
               </div>
              </div>
              <br><br>
              <div class="replace"> <div class="row" id="opexamples"> <div class="text-center col-lg-12"> <table class="table table-bordered table-hover"> <thead> <tr id="tableheader"> <th class="text-center">Operation Prediction Examples</th> </tr> </thead> <tbody> <tr id="example1" style="height:80px;overflow:hidden;cursor:pointer"> <td>Joan found 70 seashells on the beach. She gave Sam some of her seashells. She now has 27 seashells. How many seashells did she give to Sam?</td> </tr> <tr id="example2" style="height:80px;overflow:hidden;cursor:pointer"> <td>There were 28 bales of hay in the barn. Tim stacked some bales in the barn today. There are now 54 bales of hay in the barn. How many bales did he store in the barn?</td> </tr> <tr id="example3" style="height:80px;overflow:hidden;cursor:pointer"> <td>Mary is baking a cake. The recipe wants 8 cups of flour. She already put in 2 cups. How many cups does she need to add?</td> </tr> <tr id="example4" style="height:80px;overflow:hidden;cursor:pointer"> <td> Michelle played 12 basketball games this year. They were defeated during 4 games. How many games did they win?</td> </tr> <tr id="example5" style="height:80px;overflow:hidden;cursor:pointer"> <td>John is having $$5. Manohar gives to him $$7 more. How much does he have now?</td> </tr> <tr id="example6" style="height:80px;overflow:hidden;cursor:pointer"> <td>Sam had 6 apples. He gave 3 apples to Fred. How many apples does Sam have now?</td> </tr> </tbody> </table> </div> </div> </div>
      </section>

      <!-- Motivation -->
      <section id="motivation" class="bg-primary">
         <div class="container">
            <div class="row">
               <div class="col-lg-12 text-center">
                  <h2 class="section-heading text-uppercase text-white">Motivation</h2>
                  <h3 class="section-subheading text-white" id="motihead">Why did we decide to build this?</h3>
               </div>
            </div>
            <div class="row">
               <div class="col-lg-8 mx-auto text-center">
                  <p class="large text-white">We found that a disturbingly large amount of primary-grade students (5th and 6th grade) either loathed Math, or were terrified of it. To ease the burden of such students, we decided to build a web application that will solve problems from categories such as simple interest, addition/subtraction, etc.</p>
               </div>
            </div>
         </div>
      </section>

      <section id="contact">
      <div class="container">
        <div class="row">
          <div class="col-lg-8 mx-auto text-center">
            <h2 class="section-heading">Let's Get In Touch!</h2>
            
            <hr class="my-4"><p class="mb-5 text-white">Ready to contribute? That's great! Send us a pull request, or contact us on email.</p>
          </div>
        </div>
        <div class="row">
          <div class="col-lg-4 ml-auto text-center">
            <i class="fa fa-github fa-3x mb-3 sr-contact fa-inverse"></i>
            <p>
               <a href="https://github.com/purvanshi/operation-prediction" class="text-white">Fork us on Github</a>
            </p>
          </div>
          <div class="col-lg-4 mr-auto text-center">
            <i class="fa fa-envelope-o fa-3x mb-3 sr-contact fa-inverse"></i>
            <p>
              <a href="mailto:dilton@gmail.com" class="text-white">dilton@gmail.com</a>
            </p>
          </div>
        </div>
      </div>
    </section>
      <!-- Bootstrap core JavaScript -->
      <script src="/static/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
      <!-- Plugin JavaScript -->
      <script src="/static/vendor/jquery-easing/jquery.easing.min.js"></script>
      <!-- Custom scripts for this template -->
      <script src="/static/js/agency.min.js"></script>
   </body>
</html>
""")

op_page = Template("""
  <html class="gr__" lang="en">
   <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      <meta name="description" content="Solve all your problems!">
      <meta name="author" content="Siddhartha Khanooja">
      <title>Dilton - A Math Word Problem Solver</title>
      <!-- Bootstrap core CSS -->
      <link href= "/static/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
      <!-- Custom fonts for this template -->
      <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">
      <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
      <link href="https://fonts.googleapis.com/css?family=Kaushan+Script" rel="stylesheet" type="text/css">
      <link href="https://fonts.googleapis.com/css?family=Droid+Serif:400,700,400italic,700italic" rel="stylesheet" type="text/css">
      <link href="https://fonts.googleapis.com/css?family=Roboto+Slab:400,100,300,700" rel="stylesheet" type="text/css">
      <script src="https://code.jquery.com/jquery-3.2.1.min.js">
      </script>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.min.css">
      <!-- Custom styles for this template -->
      <link href= "/static/css/agency.min.css" rel="stylesheet">
      <script type="text/javascript">
         $$(document).on('click', '.table > tbody > tr', function(e){
               e.preventDefault();
               var text = $$(this).text();
               var trimmedtext = $$.trim(text);
               $$('.form-control').val(trimmedtext);
               }); 
         $$(document).on('click','#si', function(e){
               e.preventDefault();
               $$(".replace").replaceWith('<div class="replace"> <div class="row" id="siexamples"> <div class="text-center col-lg-12"> <table class="table table-bordered table-hover"> <thead> <tr id="tableheader"> <th class="text-center">Simple Interest Examples</th> </tr> </thead> <tbody> <tr id="example1" style="height:80px;overflow:hidden;cursor:pointer"> <td>What sum of money will earn an interest of $$162 in 3 years at the rate of 12% per annum?</td> </tr> <tr id="example2" style="height:80px;overflow:hidden;cursor:pointer"> <td>How much time will it take for an amount of $$900 to yield $$81 as interest at 4.5% per annum of simple interest?</td> </tr> <tr id="example3" style="height:80px;overflow:hidden;cursor:pointer"> <td>A sum fetched a total simple interest of $$929.20 at the rate of 8% per annum in 5 years. What is the sum?</td> </tr> <tr id="example4" style="height:80px;overflow:hidden;cursor:pointer"> <td>$$10,000 is invested at 5% interest rate in 1 year. Find the interest.</td> </tr> <tr id="example5" style="height:80px;overflow:hidden;cursor:pointer"> <td>$$3,500 is given at 7% p.a. rate of interest. Find the interest which will be received at the end of one year.</td> </tr> <tr id="example6" style="height:80px;overflow:hidden;cursor:pointer"> <td>If Manohar pays an interest of $$750 for 2 years on a sum of $$4,500, find the rate of interest.</td> </tr> </tbody> </table> </div> </div> </div>');
               $$("#unique").attr("action","http://127.0.0.1:5000/sipred");
               $$("#buttontext").text("Simple Interest");
         });
         $$(document).on('click','#op', function(e){
               e.preventDefault();
               $$(".replace").replaceWith('<div class="replace"> <div class="row" id="opexamples"> <div class="text-center col-lg-12"> <table class="table table-bordered table-hover"> <thead> <tr id="tableheader"> <th class="text-center">Operation Prediction Examples</th> </tr> </thead> <tbody> <tr id="example1" style="height:80px;overflow:hidden;cursor:pointer"> <td>Joan found 70 seashells on the beach. She gave Sam some of her seashells. She now has 27 seashells. How many seashells did she give to Sam?</td> </tr> <tr id="example2" style="height:80px;overflow:hidden;cursor:pointer"> <td>There were 28 bales of hay in the barn. Tim stacked some bales in the barn today. There are now 54 bales of hay in the barn. How many bales did he store in the barn?</td> </tr> <tr id="example3" style="height:80px;overflow:hidden;cursor:pointer"> <td>Mary is baking a cake. The recipe wants 8 cups of flour. She already put in 2 cups. How many cups does she need to add?</td> </tr> <tr id="example4" style="height:80px;overflow:hidden;cursor:pointer"> <td> Michelle played 12 basketball games this year. They were defeated during 4 games. How many games did they win?</td> </tr> <tr id="example5" style="height:80px;overflow:hidden;cursor:pointer"> <td>John is having $$5. Manohar gives to him $$7 more. How much does he have now?</td> </tr> <tr id="example6" style="height:80px;overflow:hidden;cursor:pointer"> <td>Sam had 6 apples. He gave 3 apples to Fred. How many apples does Sam have now?</td> </tr> </tbody> </table> </div> </div> </div>');
               $$("#unique").attr("action","http://127.0.0.1:5000/oppred");
               $$("#buttontext").text("Operation Prediction");

         });

      </script>
      <style>
         .table {
           border: 0.5px solid #000000;
         }
         .table-bordered > thead > tr > th,
         .table-bordered > tbody > tr > th,
         .table-bordered > tfoot > tr > th,
         .table-bordered > thead > tr > td,
         .table-bordered > tbody > tr > td,
         .table-bordered > tfoot > tr > td {
            border: 0.5px solid #000000;
         }
         .bg-primary, .dropdown-toggle, .rightb {
            background-color: #f05f40 !important;
         }
         a {
            color : black;
         }
         
         #start {
            padding: 50px 0;
         }

         #about, #team {
            padding: 75px 0;
         }

         #motivation {
            padding: 100px 0;
         }
         #motihead {
            margin-bottom: 50px;
         }
      </style>
   </head>
   <body id="page-top" data-gr-c-s-loaded="true" class="">
      <!-- Navigation -->
      <nav class="navbar navbar-expand-lg navbar-dark fixed-top" id="mainNav">
         <div class="container">
            <a class="navbar-brand js-scroll-trigger" href="#page-top">Dilton - The Math Word Problem Solver</a>
            <button class="navbar-toggler navbar-toggler-right collapsed" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
            Menu
            <i class="fa fa-bars"></i>
            </button>
            <div class="collapse navbar-collapse" id="navbarResponsive">
               <ul class="navbar-nav text-uppercase ml-auto">
                  <li class="nav-item">
                     <a class="nav-link js-scroll-trigger" href="#start">Start</a>
                  </li>
                  <li class="nav-item">
                     <a class="nav-link js-scroll-trigger" href="#motivation">Motivation</a>
                  </li>
                  <li class="nav-item">
                     <a class="nav-link js-scroll-trigger" href="#contact">Contact</a>
                  </li>
               </ul>
            </div>
         </div>
      </nav>
      <!-- Header -->
      <header class="masthead">
         <div class="container">
         </div>
      </header>
      <br><br><br><br><br><br>
      <img src="/static/img/omega.png" class="rounded mx-auto d-block"/>
      <!-- Input Box -->
      <section id="start">
         <div class="container">
            <div class="row">
               <div class="col-lg-12 text-center">
                  <h2 class="section-heading text-uppercase">Dilton</h2>
               </div>
            </div>
            <form action="http://127.0.0.1:5000/oppred" method="post" id="unique">
            <div class="row">
               <div class="col-lg-12">
                   <div class="input-group">
                     <div class="input-group-btn">
                       <button type="button" class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" id="buttontext">
                         Type of Question
                       </button>
                       <div class="dropdown-menu">
                         <a class="dropdown-item" href="#" id="si">Simple Interest</a>
                         <a class="dropdown-item" href="#" id="op">Operation Prediction</a>
                       </div>
                     </div>
                        <input type="text" class="form-control" aria-label="Text input with dropdown button" placeholder="Enter your question. " autocomplete="off" name="qtest">
                        <span class="input-group-btn">
                            <input type="submit"class="btn btn-secondary rightb" type="button" value="Solve!"></button>
                        </span>
                   </div>
                 </div>
              </div>
              </form>
              <div class="row">
               <div class="col-lg-8 mx-auto text-center">
                  <p class="large">The question is: </p>
                  <p> "${name}" </p>
                  <p class="large" id="answer">The answer is: </p>
                  <p> ${num1} ${op} ${num2} = ${ans}</p>
               </div>
            </div>
              <br><br>
              <div class="replace"> <div class="row" id="opexamples"> <div class="text-center col-lg-12"> <table class="table table-bordered table-hover"> <thead> <tr id="tableheader"> <th class="text-center">Operation Prediction Examples</th> </tr> </thead> <tbody> <tr id="example1" style="height:80px;overflow:hidden;cursor:pointer"> <td>Joan found 70 seashells on the beach. She gave Sam some of her seashells. She now has 27 seashells. How many seashells did she give to Sam?</td> </tr> <tr id="example2" style="height:80px;overflow:hidden;cursor:pointer"> <td>There were 28 bales of hay in the barn. Tim stacked some bales in the barn today. There are now 54 bales of hay in the barn. How many bales did he store in the barn?</td> </tr> <tr id="example3" style="height:80px;overflow:hidden;cursor:pointer"> <td>Mary is baking a cake. The recipe wants 8 cups of flour. She already put in 2 cups. How many cups does she need to add?</td> </tr> <tr id="example4" style="height:80px;overflow:hidden;cursor:pointer"> <td> Michelle played 12 basketball games this year. They were defeated during 4 games. How many games did they win?</td> </tr> <tr id="example5" style="height:80px;overflow:hidden;cursor:pointer"> <td>John is having $$5. Manohar gives to him $$7 more. How much does he have now?</td> </tr> <tr id="example6" style="height:80px;overflow:hidden;cursor:pointer"> <td>Sam had 6 apples. He gave 3 apples to Fred. How many apples does Sam have now?</td> </tr> </tbody> </table> </div> </div> </div>
      </section>

      <!-- Motivation -->
      <section id="motivation" class="bg-primary">
         <div class="container">
            <div class="row">
               <div class="col-lg-12 text-center">
                  <h2 class="section-heading text-uppercase text-white">Motivation</h2>
                  <h3 class="section-subheading text-white" id="motihead">Why did we decide to build this?</h3>
               </div>
            </div>
            <div class="row">
               <div class="col-lg-8 mx-auto text-center">
                  <p class="large text-white">We found that a disturbingly large amount of primary-grade students (5th and 6th grade) either loathed Math, or were terrified of it. To ease the burden of such students, we decided to build a web application that will solve problems from categories such as simple interest, addition/subtraction, etc.</p>
               </div>
            </div>
         </div>
      </section>

      <section id="contact">
      <div class="container">
        <div class="row">
          <div class="col-lg-8 mx-auto text-center">
            <h2 class="section-heading">Let's Get In Touch!</h2>
            
            <hr class="my-4"><p class="mb-5 text-white">Ready to contribute? That's great! Send us a pull request, or contact us on email.</p>
          </div>
        </div>
        <div class="row">
          <div class="col-lg-4 ml-auto text-center">
            <i class="fa fa-github fa-3x mb-3 sr-contact fa-inverse"></i>
            <p>
               <a href="https://github.com/purvanshi/operation-prediction" class="text-white">Fork us on Github</a>
            </p>
          </div>
          <div class="col-lg-4 mr-auto text-center">
            <i class="fa fa-envelope-o fa-3x mb-3 sr-contact fa-inverse"></i>
            <p>
              <a href="mailto:dilton@gmail.com" class="text-white">dilton@gmail.com</a>
            </p>
          </div>
        </div>
      </div>
    </section>
      <!-- Bootstrap core JavaScript -->
      <script src="/static/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
      <!-- Plugin JavaScript -->
      <script src="/static/vendor/jquery-easing/jquery.easing.min.js"></script>
      <!-- Custom scripts for this template -->
      <script src="/static/js/agency.min.js"></script>
   </body>
</html>
""")

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("mainpage.html")

@app.route('/oppredsuccess/<name>')
def oppredsuccess(name):
   # g = test.numpy.exp(2)
   operator, answer, number1, number2 = model1.main_func(name)
   number1 = float(number1)
   number2 = float(number2)
   if(operator=='-'):
      p = number1 - number2
      if(p>0):
        answer = p
        return op_page.substitute(name=name, num1=number1, num2=number2, op=operator, ans=answer)
      else:
        answer = p * (-1)
        return op_page.substitute(name=name, num1=number2, num2=number1, op=operator, ans=answer)
   return op_page.substitute(name=name, num1=number1, num2=number2, op=operator, ans=answer)

@app.route('/sipredsuccess/<name>')
def sipredsuccess(name):
   final = SI.main_func(name)
   quotes = '"'
   initial = 'python3 SI.py '
   name2 = name.replace('$', '\$')
   cmd = initial + quotes + name2 + quotes
   p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
   text = p.communicate()[0]
   #u = [x.start() for x in re.finditer('\\n', text)]
   text2 = text.decode("utf-8")
   u = [x for x, v in enumerate(text2) if v == '\n']
   start = u[len(u)-3]
   end = u[len(u)-2]
   var = text2[start+1:end]
   before_dec, after_dec = str(final).split('.')
   new_value = float('.'.join((before_dec, after_dec[0:3])))
   return si_page.substitute(name=name, siunknown=var, sianswer=new_value)

@app.route('/oppred',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['qtest']
      return redirect(url_for('oppredsuccess',name = user))
   else:
      user = request.args.get('qtest')
      return redirect(url_for('oppredsuccess',name = user))

@app.route('/sipred',methods = ['POST', 'GET'])
def login2():
   if request.method == 'POST':
      user = request.form['qtest']
      return redirect(url_for('sipredsuccess',name = user))
   else:
      user = request.args.get('qtest')
      return redirect(url_for('sipredsuccess',name = user))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
