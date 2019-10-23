<template>
<div class="container" style="margin: auto">
 <Login></Login>
</div>
</template>

<script>
import Login from '../components/Login'
export default {
  name: 'LoginPage',
  components: {
    Login
  },
  methods: {
  },
  }
</script>
<style>
  .container {
      width: 70%;
}
</style>
