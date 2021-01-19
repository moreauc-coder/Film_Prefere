
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import cgi
import cgitb
import smtplib
from email.mime.text import MIMEText
import smtplib

cgitb.enable()
form = cgi.FieldStorage()
email = ""
pseudo = ""
message = ""





print("Content-type: text/html; charset=utf-8\n")
html = """
<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../../../favicon.ico">
    <link rel="stylesheet" type="text/css" href="styles.css">
    <script src="https://kit.fontawesome.com/d7d8afdd19.js" crossorigin="anonymous"></script>
    <title>Le petit ciné</title>
    
    <!--Template based on URL below-->
    <link rel="canonical" href="https://getbootstrap.com/docs/4.3/examples/starter-template/">

    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <!-- Place your stylesheet here-->
    <link href="/css/stylesheet.css" rel="stylesheet" type="text/css">
    
</head>

<body>

<nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
    <a class="navbar-brand" href="index.html">Accueil</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarsExampleDefault">
        <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
                <a class="nav-link" href="#"> <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="Contact.html">Contact</a>
            </li>
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="dropdown01" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Mes films</a>
                <div class="dropdown-menu" aria-labelledby="dropdown01">
                    <a class="dropdown-item" href="#">Fast and Furious</a>
                    <a class="dropdown-item" href="#">Les tuches</a>
                    <a class="dropdown-item" href="JurassicPark.html">Jurassic Park</a>
                    <a class="dropdown-item" href="#">+Ajouter</a>
                </div>
            </li>
        </ul>
        
    <div class="LPC"><p class="NomSite text-warning font-weight-bold navbar-brand">Le Petit ciné</p></div>
    
    <div onclick="connection();" class="connexion">
        <a><p class="connexion_ecrit">Connection</p><i class="fas fa-user-circle" id="icon"></i></a>
<!--        onclick="alert('Non');"-->
        </div>
    </div>
</nav>

    <main role="main" class="container">
         <div class="text-center mt-5 pt-5">
            <h1>Une question sur un film? Contacte moi!</h1>
            <p class="lead"> (sauf un film romantique)</p>
        </div>
        
<!--        ici commence le formulaire-->
<form onSubmit="return formulaire()" action="Formulaire.py" method="post">
  <div class="form-group position-relative mx-auto mt-auto">
    <label for="email">Adresse mail:</label>
    <input name="email" type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Entre ton e-mail">
    <small id="emailHelp" class="form-text text-muted">Nous ne partagerons jamais votre e-mail avec qui que ce soit.(c'est faux)</small>
  </div>
  <div class="form-group">
    <label for="pseudo">Pseudo:</label>
    <input name="pseudo" class="form-control" id="pseudo" placeholder="entre ton pseudo">
  </div>
    <div class="form-group">
    <label for="msg">Message:</label>
    <textarea name="message" class="form-control" id="msg" rows="3" placeholder="entre ton message"></textarea>
  </div>
  <input type="submit" class="btn btn-primary" name="valider" value="Envoyer" id="formulaire_contact" >
</form>
"""
print(html)
if form.getvalue("email") and form.getvalue("pseudo") and form.getvalue("message") :
    email = form.getvalue("email")
    pseudo = form.getvalue("pseudo")
    message = form.getvalue("message")
    msg = MIMEMultipart()
    msg['From'] = str(email)
    msg['To'] = 'tt448723@gmail.com'
    msg['Subject'] = 'Le Petit Ciné'
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('tt448723@gmail.com', '1a2z3e4r')
    mailserver.sendmail(str(email), 'tt448723@gmail.com', msg.as_string())
    mailserver.quit()
    print("Message transmis")
else:
    print("Message non transmis")


print(str(email))
print(str(pseudo))
print(str(message))

html="""

    </main><!-- /.container -->

<!--        champs-long champs-textarea-->
    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <script type="text/javascript" src="script.js"></script>

</body>
</html>
"""
print(html)


# else:
#     raise Exception("non transmis")


# a = request.POST['email']
# b = request.POST['Message']
# c = request.POST['MotDePasse']

# print(str(a))
# print(str(b))
# print(str(c))
