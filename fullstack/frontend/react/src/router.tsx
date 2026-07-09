import {
  createRootRoute,
  createRoute,
  createRouter,
} from "@tanstack/react-router";

import App from "./App";
import Home from "./components/Home/Home_Page";

const rootRoute = createRootRoute();

const appRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: "/",
  component: App,
});

const homeRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: "/home",
  component: Home,
});

const routeTree = rootRoute.addChildren([
  appRoute,
  homeRoute,
]);

export const router = createRouter({
  routeTree,
});