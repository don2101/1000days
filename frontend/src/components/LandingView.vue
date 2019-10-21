<template>
<!--    <div>-->
<!--        <h1>Landing View</h1>-->
<!--    </div>-->
    <div id="fullpage">
        <div class="section" style="background: pink">Some section</div>
        <div class="section" style="background: ivory">Some section</div>
        <div class="section" style="background: gray">Some section</div>
        <div class="section" style="background: yellow">Some section</div>
    </div>
</template>


<script>
    export default {
        name: 'LandingView',
        data() {
            return {

            }
        },
        mounted() {
            new fullpage('#fullpage', {
                //options here
                autoScrolling:true,
                scrollHorizontally: true
            });
        }
    }
</script>

<style>

</style>