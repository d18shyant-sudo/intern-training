import { createFileRoute } from '@tanstack/react-router'

function Home() {
  return (
    <h1>
      Welcome to Home Page
    </h1>
  )
}

export const Route = createFileRoute('/home')({
  component: Home,
})