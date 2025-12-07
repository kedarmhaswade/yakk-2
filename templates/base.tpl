<!-- base.tpl -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{{ title }}</title>

    <!-- CDN frameworks -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/normalize.css@8.0.1/normalize.css" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/sakura.css/css/sakura.css" />

    <!-- Local overrides -->
    <link rel="stylesheet" href="style.css" />
</head>
<body>
    <nav class="blog-nav">
        <a href="index.html">Home</a>
    </nav>

    <main>
        {{ content }}
    </main>
</body>
</html>
