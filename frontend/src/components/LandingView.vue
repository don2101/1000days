<template>
    <div id="fullpage">
        <div class="section">
            <img src="../images/LandingView/holdingHand-black.jpg" width="100%" height="100%" alt="">
        </div>
        <div class="section">
            <img src="../images/LandingView/baby-feet-4260035_640.jpg" width="100%" height="100%" alt="">
        </div>
        <div class="section">
            <img src="../images/LandingView/embracedBaby.jpg" width="100%" height="100%" alt="">
        </div>
        <div class="section">
            <img src="../images/LandingView/family.jpg" width="100%" height="100%" alt="">
        </div>
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