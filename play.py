with open('play.html', 'w') as f:
    f.write('''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Python</title>
    <link rel="stylesheet" href="play.css">
</head>
    <body>
        <h1>Hello World From Python</h1>
        <table>
            <tr>
                <th>Table Test</th>
                <th>Table Test</th>
                <th>Table Test</th>
            </tr>
            <tr>
                <td>Help</td>
                <td>Help</td>
                <td>Help</td>
            </tr>
        </table>
    </body>
</html>''')

with open('play.css', 'w') as c:
    c.write('''h1 {
    color: blue;
    font-size: 80px;
}


@media (min-width: 600px) and (max-width: 800px){
    h1 {
        color: yellow;
        font-size: 60px;
    }
}

@media (min-width: 100px) and (max-width: 600px) {
    h1 {
        color: green;
        font-size: 40px;
    }
}''')