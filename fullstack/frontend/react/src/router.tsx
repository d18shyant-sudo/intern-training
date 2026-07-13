import { createRootRoute, createRoute, createRouter, Outlet } from '@tanstack/react-router'
import App from './App'
import Form from './components/form/form';
import Add_User from './components/form/adduser';
import ViewUsers from './components/form/viewuser';
import Edit_User from './components/form/Edit_User';
import { Toaster } from 'react-hot-toast';
import  Signup  from './components/login/signup';

const rootRoute = createRootRoute({
  component: ()=>  (<>
      <Toaster position="top-right" />
      <Outlet />
    </>),
});

const indexRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: '/',
  component: App,
});

const  formRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: '/form',
  component: Form,
})
const  useraddRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: '/add_user',
  component: Add_User,
})
const  userviewRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: '/view_user',
  component: ViewUsers,
})
const editUserRoute = createRoute({
  getParentRoute:()=>rootRoute,
  path:'/edit_user/$email',
  component:Edit_User
});
const signupRoute = createRoute({
  getParentRoute:()=>rootRoute,
  path:'/sign_up',
  component:Signup
});
const routeTree = rootRoute.addChildren([
  indexRoute,
  formRoute,
  useraddRoute,
  userviewRoute,
  editUserRoute,
  signupRoute
]);

export const router = createRouter({
  routeTree,
});
