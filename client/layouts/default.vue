<template>
	<v-app>
		<Header class="z-index-12" />
		<v-main>
			<v-container v-if="isLoggedIn">
				<Nuxt class="z-index-1" />
				<div id="vk_community_messages"></div>
			</v-container>
		</v-main>
		<Footer class="z-index-10" />
	</v-app>
</template>

<script>
import Header from '@/components/UI/Header.vue'
import Footer from '@/components/UI/Footer.vue'
import {mapState} from "vuex"
export default {
	name: 'DefaultLayout',
	components: {
		Header,
		Footer
	},
	data() {
		return ({
			counter: 0,
			user: false,
		})
	},
	computed:{
		...mapState("auth", ["isLoggedIn", "accessToken"])
	}
}
</script>

<style>
.z-index-12 {
	z-index: 12;
}
</style>

