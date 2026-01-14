# Template : App Layout
**Fichier cible** : `app/templates/app-layout.html`

---

## **Description**
Layout principal utilisé par le blueprint `app` et `auth`. Contient la sidebar, topbar et espace contenu. Inspiré de Flowbite pour une expérience professionnelle.

---

## **Structure HTML**
```html
{% extends "base.html" %}

{% block content %}
<div class="flex h-screen bg-bg-light" x-data="appLayoutState()">
  <!-- Sidebar -->
  {% include "partials/sidebar.html" %}
  
  <!-- Main Content Area -->
  <div class="flex flex-col flex-1">
    <!-- Topbar -->
    {% include "partials/topbar.html" %}
    
    <!-- Content -->
    <main class="flex-1 overflow-auto p-6">
      {% block page_content %}{% endblock %}
    </main>
  </div>
</div>
{% endblock %}

{% block scripts %}
<script>
  function appLayoutState() {
    return {
      user: {},
      isLoading: true,
      
      async loadUser() {
        try {
          const response = await fetch('/api/user/info');
          const data = await response.json();
          this.user = data.user;
        } catch (error) {
          console.error('Erreur chargement user:', error);
        } finally {
          this.isLoading = false;
        }
      },
      
      init() {
        this.loadUser();
      }
    };
  }
</script>
{% endblock %}
```

---

## **Blocs Hérités**
- `{% block page_content %}` : Contenu principal de la page
- `{% block scripts %}` : Scripts supplémentaires
