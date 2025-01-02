<template>
    <header>
        <nav>
            <h1>股票分析</h1>
            <div class="auth-container">
                <router-link to="/login">登入</router-link>
                <router-link to="/register">註冊</router-link>
            </div>
        </nav>
    </header>
</template>

<script>
export default {
    name: 'Navbar'
}
</script>

<style>
nav{
    display: flex;
    justify-content: space-between;
    background-color: #F5F5DC;
}
nav h1{
    margin-left: 20px;
}
.auth-container{
    width: 10%;
    display: flex;
    gap: 15%;
    align-items: center;
    justify-content: center;
    font-size: 20px;
}
.auth-container a {
    text-decoration: none;
    color: black;
}
</style>