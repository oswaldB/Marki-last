# Partial : Topbar
**Fichier cible** : `app/templates/partials/topbar.html`

---

## **Description**
Barre supérieure affichant les infos utilisateur, notifications et menu déroulant.

---

## **Structure HTML**
```html
<header class="bg-white border-b border-border shadow-sm" x-data="topbarState()">
  <div class="flex items-center justify-between px-6 py-4">
    <!-- Left: Sidebar Toggle (Mobile) -->
    <div class="md:hidden">
      <button @click="$root.isOpen = !$root.isOpen" class="p-2 hover:bg-bg-light rounded-lg">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
        </svg>
      </button>
    </div>

    <!-- Center: Title -->
    <h1 class="text-2xl font-bold text-text md:block hidden"></h1>

    <!-- Right: Notifications & User Menu -->
    <div class="flex items-center gap-6">
      <!-- Notifications -->
      <div class="relative">
        <button class="relative p-2 hover:bg-bg-light rounded-lg transition-colors"
                @click="showNotifications = !showNotifications">
          <svg class="w-6 h-6 text-text" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"></path>
          </svg>
          <span class="absolute top-1 right-1 w-2 h-2 bg-error rounded-full" x-show="notifications.length > 0"></span>
        </button>

        <!-- Notifications Dropdown -->
        <div class="absolute right-0 mt-2 w-80 bg-white border border-border rounded-lg shadow-lg z-50"
             x-show="showNotifications" @click.away="showNotifications = false">
          <div class="p-4 border-b border-border">
            <h3 class="font-semibold text-text">Notifications</h3>
          </div>
          <div class="divide-y divide-border max-h-80 overflow-y-auto">
            <template x-for="notif in notifications" :key="notif.id">
              <div class="p-4 hover:bg-bg-light transition-colors">
                <p class="text-sm text-text" x-text="notif.message"></p>
              </div>
            </template>
            <div x-show="notifications.length === 0" class="p-4 text-center text-text-light">
              Aucune notification
            </div>
          </div>
        </div>
      </div>

      <!-- User Menu -->
      <div class="relative">
        <button class="flex items-center gap-2 p-2 hover:bg-bg-light rounded-lg transition-colors"
                @click="showUserMenu = !showUserMenu">
          <div class="w-8 h-8 bg-primary rounded-full flex items-center justify-center text-white text-sm font-bold"
               x-text="user.username?.charAt(0).toUpperCase()"></div>
          <span class="hidden md:inline text-sm font-medium text-text" x-text="user.username"></span>
        </button>

        <!-- User Dropdown Menu -->
        <div class="absolute right-0 mt-2 w-48 bg-white border border-border rounded-lg shadow-lg z-50"
             x-show="showUserMenu" @click.away="showUserMenu = false">
          <div class="p-4 border-b border-border">
            <p class="text-sm font-semibold text-text" x-text="user.username"></p>
            <p class="text-xs text-text-light" x-text="user.email"></p>
          </div>
          <ul class="divide-y divide-border">
            <li>
              <a href="/profile" class="block px-4 py-3 text-sm text-text hover:bg-bg-light transition-colors">
                Mon Profil
              </a>
            </li>
            <li x-show="user.isAdmin">
              <a href="/settings/team" class="block px-4 py-3 text-sm text-text hover:bg-bg-light transition-colors">
                Équipe
              </a>
            </li>
            <li>
              <form action="/auth/logout" method="POST" class="block">
                <button type="submit" class="w-full text-left px-4 py-3 text-sm text-error hover:bg-bg-light transition-colors">
                  Déconnexion
                </button>
              </form>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</header>

<script>
  function topbarState() {
    return {
      user: Alpine.$data(document.querySelector('[x-data="appLayoutState()"]')).user,
      showUserMenu: false,
      showNotifications: false,
      notifications: []
    };
  }
</script>
```
