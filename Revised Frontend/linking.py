from flask import Flask, redirect, url_for, request, render_template
import model1
from string import Template

index_page = Template("""
  <html class="gr__" lang="en">
   <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      <meta name="description" content="">
      <meta name="author" content="">
      <title>Dilton - A Math Word Problem Solver</title>
      <!-- Bootstrap core CSS -->
      <link href= "/static/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
      <!-- Custom fonts for this template -->
      <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">
      <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
      <link href="https://fonts.googleapis.com/css?family=Kaushan+Script" rel="stylesheet" type="text/css">
      <link href="https://fonts.googleapis.com/css?family=Droid+Serif:400,700,400italic,700italic" rel="stylesheet" type="text/css">
      <link href="https://fonts.googleapis.com/css?family=Roboto+Slab:400,100,300,700" rel="stylesheet" type="text/css">
      <script
           src="https://code.jquery.com/jquery-3.2.1.min.js"
           integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
           crossorigin="anonymous">
      </script>
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
               $$(".replace").replaceWith('<div class="replace"> <div class="row" id="siexamples"> <div class="text-center col-lg-12"> <table class="table table-bordered table-hover"> <thead> <tr id="tableheader"> <th class="text-center">Simple Interest Examples</th> </tr> </thead> <tbody> <tr id="example1" style="height:80px;overflow:hidden;cursor:pointer"> <td>What sum of money will earn an interest of $$162 in 3 years at the rate of 12% per annum?</td> </tr> <tr id="example2" style="height:80px;overflow:hidden;cursor:pointer"> <td>How much time will it take for an amount of $$900 to yield $$81 as interest at 4.5% per annum of simple interest?</td> </tr> <tr id="example3" style="height:80px;overflow:hidden;cursor:pointer"> <td>A sum fetched a total simple interest of $$929.20 at the rate of 8% per annum in 5 years. What is the sum?</td> </tr> <tr id="example4" style="height:80px;overflow:hidden;cursor:pointer"> <td>$$10,000 is invested at 5% interest rate in 1 year. Find the interest.</td> </tr> <tr id="example5" style="height:80px;overflow:hidden;cursor:pointer"> <td>$$3,500 is given at 7% p.a. rate of interest. Find the interest which will be received at the end of two years.</td> </tr> <tr id="example6" style="height:80px;overflow:hidden;cursor:pointer"> <td>If Manohar pays an interest of $$750 for 2 years on a sum of $$4,500, find the rate of interest.</td> </tr> </tbody> </table> </div> </div> </div>');
         });
         $$(document).on('click','#op', function(e){
               e.preventDefault();
               $$(".replace").replaceWith('<div class="replace"> <div class="row" id="opexamples"> <div class="text-center col-lg-12"> <table class="table table-bordered table-hover"> <thead> <tr id="tableheader"> <th class="text-center">Operation Prediction Examples</th> </tr> </thead> <tbody> <tr id="example1" style="height:80px;overflow:hidden;cursor:pointer"> <td>Joan found 70 seashells on the beach. She gave Sam some of her seashells. She now has 27 seashells. How many seashells did she give to Sam?</td> </tr> <tr id="example2" style="height:80px;overflow:hidden;cursor:pointer"> <td>There were 28 bales of hay in the barn. Tim stacked some bales in the barn today. There are now 54 bales of hay in the barn. How many bales did he store in the barn?</td> </tr> <tr id="example3" style="height:80px;overflow:hidden;cursor:pointer"> <td>Mary is baking a cake. The recipe wants 8 cups of flour. She already put in 2 cups. How many cups does she need to add?</td> </tr> <tr id="example4" style="height:80px;overflow:hidden;cursor:pointer"> <td> Michelle played 12 basketball games this year. They were defeated during 4 games. How many games did they win?</td> </tr> <tr id="example5" style="height:80px;overflow:hidden;cursor:pointer"> <td>John is having $$5. Manohar gives to him $$7 more. How much does he have now?</td> </tr> <tr id="example6" style="height:80px;overflow:hidden;cursor:pointer"> <td>Sam had 6 apples. He gave 3 apples to Fred. How many apples does Sam have now?</td> </tr> </tbody> </table> </div> </div> </div>');
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
            <a class="navbar-brand js-scroll-trigger" href="#page-top">Dilton - Solve all your problems!</a>
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
                     <a class="nav-link js-scroll-trigger" href="#about">About</a>
                  </li>
                  <li class="nav-item">
                     <a class="nav-link js-scroll-trigger" href="#team">Our Team</a>
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
                  <h3 class="section-subheading text-muted">The Math Word Problem Solver. </h3>
               </div>
            </div>
            <form action="http://127.0.0.1:5000/test" method="post">
            <div class="row">
               <div class="col-lg-12">
                   <div class="input-group">
                     <div class="input-group-btn">
                       <button type="button" class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                         Select your option
                       </button>
                       <div class="dropdown-menu">
                         <a class="dropdown-item" href="#" id="si">Simple Interest</a>
                         <a class="dropdown-item" href="#" id="op">Operation Prediction</a>
                         <div role="separator" class="dropdown-divider"></div>
                         <a class="dropdown-item" href="#" id="se">Sequence Encoder</a>
                       </div>
                     </div>
                        <input type="text" class="form-control" aria-label="Text input with dropdown button" placeholder="Enter your question. " autocomplete="off" name="qtest">
                        <span class="input-group-btn">
                            <input type="submit"class="btn btn-secondary rightb" type="button" value="Go!"></button>
                        </span>
                   </div>
                 </div>
              </div>
              </form>
              <div class="row">
               <div class="col-lg-8 mx-auto text-center">
                  <p class="large">The answer is ${ans} and operator is ${op}.</p>
               </div>
            </div>
              <br><br>
              <div class="replace">
              <div class="row" id="siexamples">
               <div class="col-lg-12 text-center">
                  <table class="table table-hover table-bordered">
                      <thead>
                        <tr id="tableheader">
                          <th class="text-center">Simple Interest Examples</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr style="height: 80px; overflow: hidden; cursor: pointer;" id="example1">
                          <td>What sum of money will earn an interest of $$162 in 3 years at the rate of 12% per annum?</td>
                        </tr>
                        <tr style="height: 80px; overflow: hidden; cursor: pointer;" id="example2">
                          <td>How much time will it take for an amount of $$900 to yield $$81 as interest at 4.5% per annum of simple interest?</td>
                        </tr>
                        <tr style="height: 80px; overflow: hidden; cursor: pointer;" id="example3">
                          <td>A sum fetched a total simple interest of $$929.20 at the rate of 8% per annum in 5 years. What is the sum?</td>
                        </tr>
                        <tr style="height: 80px; overflow: hidden; cursor: pointer;" id="example4">
                          <td>$$10,000 is invested at a rate of 5% per annum for 1 year. Find the interest.</td>
                        </tr>
                        <tr style="height: 80px; overflow: hidden; cursor: pointer;" id="example5">
                          <td>$$3,500 is given at 7% p.a. rate of interest. Find the interest which will be received at the end of two years.</td>
                        </tr>
                        <tr style="height: 80px; overflow: hidden; cursor: pointer;" id="example6">
                          <td>If Manohar pays an interest of $$750 for 2 years on a sum of $$4,500, find the rate of interest.</td>
                        </tr>
                      </tbody>
                  </table>
               </div>
            </div>
         </div>
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

      <!-- Timeline -->
      <section id="about">
         <div class="container">
            <div class="row">
               <div class="col-lg-12 text-center">
                  <h2 class="section-heading text-uppercase">About</h2>
                  <h3 class="section-subheading text-muted">A visual timeline of our efforts.</h3>
               </div>
            </div>
            <div class="row">
               <div class="col-lg-12">
                  <ul class="timeline">
                     <li>
                        <div class="timeline-image">
                           <img class="rounded-circle img-fluid" src="/static/img/man-thinking.png" alt="">
                        </div>
                        <div class="timeline-panel">
                           <div class="timeline-heading">
                              <h4>February - March</h4>
                              <h4 class="subheading">From Humble Beginnings</h4>
                           </div>
                           <div class="timeline-body">
                              <p class="text-muted">These months were spent on scouring endless research papers to study experimental methods for solving word problems. We also spent an inordinate amount of time manually collecting problems, and manually solving and tagging them. At this point, we were (mostly) stumbling in the dark, looking for light at the end of the tunnel. </p>
                           </div>
                        </div>
                     </li>
                     <li class="timeline-inverted">
                        <div class="timeline-image">
                           <img class="rounded-circle img-fluid" src="/static/img/brainstorm.png" alt="">
                        </div>
                        <div class="timeline-panel">
                           <div class="timeline-heading">
                              <h4>April - May</h4>
                              <h4 class="subheading">Revelations - Part I</h4>
                           </div>
                           <div class="timeline-body">
                              <p class="text-muted">This period was marked by us successfully solving Simple Interest problems (that were not arbitrarily worded) with an accuracy of more than 90%. We also made the first iteration of our site, which was, in hindsight, quite hideous. </p>
                           </div>
                        </div>
                     </li>
                     <li>
                        <div class="timeline-image">
                           <img class="rounded-circle img-fluid" src="/static/img/think.png" alt="">
                        </div>
                        <div class="timeline-panel">
                           <div class="timeline-heading">
                              <h4>June - September</h4>
                              <h4 class="subheading">Struggles</h4>
                           </div>
                           <div class="timeline-body">
                              <p class="text-muted">These months were spent partly in frustration, with no outlets for venting - we couldn't scale the steep learning curve of AWS. So, we decided to focus our efforts on solving another category of problems - namely, those involving one operation - +/-/* etc. We could only make some headway, as we were still trying to solve the problems through NLTK. </p>
                           </div>
                        </div>
                     </li>
                     <li class="timeline-inverted">
                        <div class="timeline-image">
                           <img class="rounded-circle img-fluid" src="/static/img/motivation.png" alt="">
                        </div>
                        <div class="timeline-panel">
                           <div class="timeline-heading">
                              <h4>October - Present</h4>
                              <h4 class="subheading">Revelations - Part II</h4>
                           </div>
                           <div class="timeline-body">
                              <p class="text-muted">These months were an eye-opener. We discovered the joys of deep learning, and used Tensorflow to predict the operation and solve word problems involving simple addition, subtraction and multiplication with an accuracy of 91%. Our future plans include incorporating sequence encoders to solve simple simple algebra problems, a complete overhaul of our site, and even visualization! </p>
                           </div>
                        </div>
                     </li>
                     <li class="timeline-inverted">
                        <div class="timeline-image">
                           <h4>Stay Tuned
                              <br>for
                              <br>More!
                           </h4>
                        </div>
                     </li>
                  </ul>
               </div>
            </div>
         </div>
      </section>

      <!-- Team -->
      <section class="bg-light" id="team">
         <div class="container">
            <div class="row">
               <div class="col-lg-12 text-center">
                  <h2 class="section-heading text-uppercase">Meet the team</h2>
                  <h3 class="section-subheading text-muted">The people that made this project possible.</h3>
               </div>
            </div>
            <div class="row">
               <div class="col-sm-4">
                  <div class="team-member">
                     <img class="mx-auto rounded-circle" src="/static/img/team/1.jpg" alt="" title="" style="">
                     <h4>Purvanshi Mehta</h4>
                     <p class="text-muted">Software Developer</p>
                     <ul class="list-inline">
                        <li class="list-inline-item">
                           <a href="https://github.com/purvanshi">
                              <span class="fa-stack fa-lg">
                                 <i class="fa fa-circle fa-stack-2x"></i>
                                 <i class="fa fa-github fa-stack-1x fa-inverse"></i>
                              </span>
                           </a>
                        </li>
                        <li class="list-inline-item">
                           <a href="https://www.facebook.com/profile.php?id=100005469885890">
                              <span class="fa-stack fa-lg">
                                 <i class="fa fa-circle fa-stack-2x"></i>
                                 <i class="fa fa-facebook fa-stack-1x fa-inverse"></i>
                              </span>
                           </a>
                        </li>
                        <li class="list-inline-item">
                           <a href="https://www.linkedin.com/in/purvanshi-mehta-305809120/">
                              <span class="fa-stack fa-lg">
                                 <i class="fa fa-circle fa-stack-2x"></i>
                                 <i class="fa fa-linkedin fa-stack-1x fa-inverse"></i>
                              </span>
                           </a>
                        </li>
                     </ul>
                  </div>
               </div>
               <div class="col-sm-4">
                  <div class="team-member">
                     <img class="mx-auto rounded-circle" src="/static/img/team/2.jpg" alt="" title="" style="">
                     <h4>Siddhartha Khanooja</h4>
                     <p class="text-muted">Software Developer</p>
                     <ul class="list-inline">
                        <li class="list-inline-item">
                           <a href="https://github.com/sidrocks123">
                              <span class="fa-stack fa-lg">
                                 <i class="fa fa-circle fa-stack-2x"></i>
                                 <i class="fa fa-github fa-stack-1x fa-inverse"></i>
                              </span>
                           </a>
                        </li>
                        <li class="list-inline-item">
                           <a href="https://www.facebook.com/SidKhanooja">
                              <span class="fa-stack fa-lg">
                                 <i class="fa fa-circle fa-stack-2x"></i>
                                 <i class="fa fa-facebook fa-stack-1x fa-inverse"></i>
                              </span>
                           </a>
                        </li>
                        <li class="list-inline-item">
                           <a href="https://www.linkedin.com/in/siddharthakhanooja/">
                              <span class="fa-stack fa-lg">
                                 <i class="fa fa-circle fa-stack-2x"></i>
                                 <i class="fa fa-linkedin fa-stack-1x fa-inverse"></i>
                              </span>
                           </a>
                        </li>
                     </ul>
                  </div>
               </div>
               <div class="col-sm-4">
                  <div class="team-member">
                     <img class="mx-auto rounded-circle" src="/static/img/team/3.jpg" alt="" title="">
                     <h4>Shreyas Kapoor</h4>
                     <p class="text-muted">Maintainer and Technical Writer</p>
                     <ul class="list-inline">
                        <li class="list-inline-item">
                           <a href="#">
                              <span class="fa-stack fa-lg">
                                 <i class="fa fa-circle fa-stack-2x"></i>
                                 <i class="fa fa-github fa-stack-1x fa-inverse"></i>
                              </span>
                           </a>
                        </li>
                        <li class="list-inline-item">
                           <a href="https://www.facebook.com/shreyas.kapoor22">
                              <span class="fa-stack fa-lg">
                                 <i class="fa fa-circle fa-stack-2x"></i>
                                 <i class="fa fa-facebook fa-stack-1x fa-inverse"></i>
                              </span>
                           </a>
                        </li>
                        <li class="list-inline-item">
                           <a href="https://www.linkedin.com/in/shreyas-kapoor-61454098/">
                              <span class="fa-stack fa-lg">
                                 <i class="fa fa-circle fa-stack-2x"></i>
                                 <i class="fa fa-linkedin fa-stack-1x fa-inverse"></i>
                              </span>
                           </a>
                        </li>
                     </ul>
                  </div>
               </div>
            </div>
            <div class="row">
               <div class="col-lg-8 mx-auto text-center">
                  <p class="large text-muted">Want your name featured here? Click <a class="js-scroll-trigger" href="#contact">here</a> to know more!</p>
               </div>
            </div>
         </div>
      </section>

      <section class="bg-primary" id="contact">
      <div class="container">
        <div class="row">
          <div class="col-lg-8 mx-auto text-center">
            <h2 class="section-heading">Let's Get In Touch!</h2>
            
            <hr class="my-4"><p class="mb-5 text-white">Ready to contribute? That's great! Send us a pull request, or contact us on email.</p>
          </div>
        </div>
        <div class="row">
          <div class="col-lg-4 ml-auto text-center">
            <i class="fa fa-github fa-3x mb-3 sr-contact"></i>
            <p>
               <a href="https://github.com/purvanshi/operation-prediction" class="text-white">Fork us on Github</a>
            </p>
          </div>
          <div class="col-lg-4 mr-auto text-center">
            <i class="fa fa-envelope-o fa-3x mb-3 sr-contact"></i>
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
      <!-- Contact form JavaScript
      <script src="/static/js/jqBootstrapValidation.js"></script>
      <script src="/static/js/contact_me.js"></script>
      -->
      <!-- Custom scripts for this template -->
      <script src="/static/js/agency.min.js"></script>
   </body>
</html>
""")

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("mainpage.html")

@app.route('/success/<name>')
def success(name):
   # g = test.numpy.exp(2)
   operator, answer = model1.main_func(name)
   return index_page.substitute(op=operator, ans=answer)

@app.route('/test',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['qtest']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('qtest')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
