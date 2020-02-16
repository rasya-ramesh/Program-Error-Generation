<!DOCTYPE html>
<html>
  <head>

    <title>CodeLearn</title>
    <link rel="stylesheet" href="css/style.css" type="text/css">
    <script type="text/javascript" src="index.js"></script>
  </head>

  <body>

    <div class="topnav">
      <a class="active" href="#home">Home</a>
      <a href="#languages">Languages</a>
      <a href="#about">About</a>
      <a href="#contact">Contact Us</a>
      <a href="login.html" id="logout" >Log Out</a>
    </div>

    <div class="intro">
      <p>Select a language  from below. The syntacticaly incorrect program will be displayed
        in the editor on the right. Make corrections to the displayed code and submit when you think
        you have made all possible corrections.</p>
    </div>
    <hr>
    <div class="body">

        <div class="split left">

          <form>
              <h2>Select Language:</h2>
              <label class="container">Python
                <input type="radio" checked="checked" name="radio">
                <span class="checkmark"></span>
              </label>
              <label class="container">C
                <input type="radio" name="radio">
                <span class="checkmark"></span>
              </label>
              <label class="container">C++
                <input type="radio" name="radio">
                <span class="checkmark"></span>
              </label>
              <button class="generate_code" onclick="fetch_code()">FETCH CODE</button>

          </form>

        </div>

        <div class="split right">

            <h2>Code Segment: </h2>
            <textarea id="codesegment" wrap=on rows="20" cols="140"><?php include('foo.txt'); ?>

            </textarea>
            <input type="submit" class="submit" value="SUBMIT" ></input>

        </div>

        <div class="split right-most">
          <h2>Score: </h2>
            <h1 id="score">10</h1>
        </div>

    </div>

  </body>
</html>
