from cgi import parse_qs, escape

html = """
<html lang="en"><head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Jumbotron Template for Bootstrap</title>

    <!-- Bootstrap core CSS -->
    <link href="http://www.ceilicornelison.com/sep/assets/css/bootstrap.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="http://www.ceilicornelison.com/sep/assets/css/custom.css" rel="stylesheet">

  </head>

  <body style="">

    <!-- Main jumbotron for a primary marketing message or call to action -->
    <div class="jumbotron">
      <div class="container">
        <h1>Simple English Parser</h1>
        <p>Simple English Parser a tool to check if your writing is easy to understand. Put your text in to the box below and press the button. Then you will get a score. Simple English Parser uses the <a href="#">Basic English Language</a> developed by Charles Kay Ogden. You can find more about him <a href="#">here.</a></p>
      </div>
    </div>

    <div class="container">
      <!-- Example row of columns -->
      <div class="row">
        <div class="col-lg-8">
          <h2>Put your text here:</h2>
          <form role="form" method="post" action="parsing_post.wsgi">
            <div class="form-group">
              <textarea id="notsimple" class="form-control" name="notsimple" rows="10"></textarea>
            </div>
            <button type="submit" class="btn btn-custom btn-lg">View details &raquo;</button>
          </form>
        </div>
        <div id="result-column" class="col-lg-4">
          <h2>Result</h2>
          <p class="result-percent">%s</p>
          <p>Your English is about %%%s simple.</p>
       </div>
      </div>

      <hr>

      <footer>
        <p>&copy; 2013 by <a href="http://www.ceilicornelison.com/">Ceili Cornelison</a></p>
        <p>Simple English Parser is licensed under a <a href="http://opensource.org/licenses/isc-license.txt">ISC License.</a></p>
      </footer>
    </div> <!-- /container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="http://codeorigin.jquery.com/jquery-2.0.3.min.js"></script>
    <script src="http://www.ceilicornelison.com/sep/assets/js/bootstrap.min.js"></script>

</body>
</html>
"""
def application(environ, start_response):

   # the environment variable CONTENT_LENGTH may be empty or missing
   try:
      request_body_size = int(environ.get('CONTENT_LENGTH', 0))
   except (ValueError):
      request_body_size = 0

   # When the method is POST the query string will be sent
   # in the HTTP request body which is passed by the WSGI server
   # in the file like wsgi.input environment variable.
   request_body = environ['wsgi.input'].read(request_body_size)
   d = parse_qs(request_body)

   notsimple = d.get('notsimple', [''])[0]

   notsimple = escape(notsimple)

   response_body = html % (notsimple or 'Empty', notsimple or 'Empty')

   status = '200 OK'

   response_headers = [('Content-Type', 'text/html'),
                  ('Content-Length', str(len(response_body)))]
   start_response(status, response_headers)

   return [response_body]
