
var view = "dashboard";
var currUser = [];
var usersJSON = [{"_id":"5a5f77566ed04917c209d011","name":"Merie","email":"tlorking0@ebay.co.uk","password":"$2a$10$Og6nfi/bS7JZcyqMY8uz2uJmfh4EGDQrN..GYVlYVkzfe1BJR245i","__v":0,"favoriteSpots":[]},{"_id":"5a5f815c274ce5189f8bda55","name":"Martynne","email":"mparkman5@t-online.de","password":"$2a$10$RCTAPEhlic0AU1E0lC/4oOoGMfeuPor0TaWlx.9grjimPxBjKl3n.","__v":0,"favoriteSpots":["143","23","965","43"]},{"_id":"5a5f8163274ce5189f8bda56","name":"Nert","email":"nheineke6@yellowbook.com","password":"$2a$10$So1JgjFKyLcKplw4YY8IvubfFD6Wnwnw1HM.HMTOjtuVvbxG0frNK","__v":0,"favoriteSpots":["143","23","965","43"]},{"_id":"5a5f8169274ce5189f8bda57","name":"Ame","email":"afillimore7@freewebs.com","password":"$2a$10$3pQ/8HEFErN7KN906J/saO4w/cBJUKyYPHkwWRpsHxhZ2idP//MY2","__v":0,"favoriteSpots":["55"]},{"_id":"5a5f8186274ce5189f8bda5a","name":null,"email":"wdudinb@dagondesign.com","password":"$2a$10$hcFqH6igieBWstb91D1aiOKZHZ2.ILefTiHSa7orYulVgDwH1qw4a","__v":0,"favoriteSpots":null},{"_id":"5a5f818c274ce5189f8bda5b","name":"Freddi","email":"fsleighc@purevolume.com","password":"$2a$10$zXUzLU.2x9Hp6RVF6ANcoe8C92CzeDchtJlYbSWvS6utCsToIGvha","__v":0,"favoriteSpots":["143","23","965","43"]},{"_id":"5a5f8198274ce5189f8bda5d","name":"Syman","email":"smagsone@is.gd","password":"$2a$10$ctG0BraaQ/IMuMQGurw3RuisIPsKo8QDvYDtxKU6izSXmx/hGl3F2","__v":0,"favoriteSpots":["3","576","223","856"]},{"_id":"5a60bdcfe48ce700145dcbce","name":"Testuser Foo","email":"foo@example.com","password":"$2a$10$bG7HoNYd/pTaznCiaqbymupHGC6f6AaVYu3SYTb3sxU9fJUecAWDu","__v":0,"favoriteSpots":["Spot 1","Spot 987"]},{"_id":"5a60c2f77c5f7043d0a6cfa1","name":"Redd","email":"rcamerello1h@examiner.com","password":"$2a$10$TCH05dZ444XdrFdZdi87Vulc2M/QjovbiqmJRg3GHntold7TvJRnC","__v":0,"favoriteSpots":null},{"_id":"5a60c3017c5f7043d0a6cfa2","name":"Wynn","email":"wgimblett1i@xinhuanet.com","password":"$2a$10$AzcJPgg2RHkAhTU/gjlEA.qUQdBhgLWRx9P33EHiYSpaBdEjcTC9i","__v":0,"favoriteSpots":["143","23","965","43"]}]


Vue.component('user-item', {

    props: ['user'],
    template:
    '<tr>' +
        '<th scope="row">{{user.index}}</th>' +
        '<td>{{ user._id }}</td>' +
        '<td>{{ user.name }}</td>' +
        '<td>{{ user.email }}</td>' +
        '<td>' +
            '<p>' +
                '<a class="btn btn-outline-secondary btn-sm" v-if="!see" v-on:click="see= !see" data-toggle="collapse"  role="button" aria-expanded="false" aria-controls="collapseExample">show Password</a>' +
            '</p>' +
            '<div class="password-box" v-if="see">' +
                '<h2>Gotcha!</h2>' +
                '<p>So you really want to fetch the password from the DB? <br> Okay, just take it.</p>' +
                '<a class="btn btn-danger btn-sm" v-on:click="see= !see" data-toggle="collapse"  role="button" aria-expanded="false" aria-controls="collapseExample">hide Password</a>' +
                '<span class="bold"> {{ user.password }} </span>' +
                 '<br><br><p> Yep, it \'\ s a hash.</p>' +
            '</div>' +
        '</td>' +
        '<td>' +
            '<button type="button" v-on:click="setPopUp(1)" class="btn btn-primary  btn-sm">Edit</button>'+
            '<button type="button" v-on:click="setPopUp(2)"  class="btn btn-danger  btn-sm">Delete</button>' +
        '</td>' +
    '</tr>',
    data: function () {
        return {
            see: false
        }
    },
    methods: {
        setPopUp: function (num) {
            currUser = this.user;
            if(num == 1) {
                this.$emit('edit');
            }
            else {
                this.$emit('delete');
            }
        }
    }

});

new Vue({
    el: '#dashboard',
    data: {
        view: view,
        popup: '',
        currUser: currUser,
        latestUser: [],
        total: 0,
        users: [],
        errors: [],
        errorMessage: '',
        email: '',
        password: '',
        name: ''
    },
    computed: {
        view: function() {
            return this.view;
        },
        popup: function () {
            return popup;
        },
        users: function () {
            this.latestUser =  jsonObject.users[jsonObject.users.length-1].email;
            return users;
        },
        currUser: function () {
            return this.currUser();
        },
        cUserId: function() {
            return this.currUser._id;
        },
        cUserEmail: function() {
            return this.currUser.email;
        },
        cUserPassword: function() {
            return this.currUser.password;
        },
        cUserName: function() {
            return this.currUser.name;
        },
        errorMessage: function() {
            return this.errorMessage;
        }
    },

    methods: {
        addUsersIndex() {
            for (const [i, user] of this.users.entries()) {
                user["index"] = i;
            }
        },
        getUsers() {
                this.users = usersJSON;
                this.total = Object.keys(this.users).length;
                var latest =  this.users[this.total - 1];
                this.latestUser =  'name:' + latest.name + '  email: ' +  latest.email ;
                this.addUsersIndex();
        },
        updateUser() {
            var postBody = this.currUser;

            postBody.id = this.currUser._id;
            //check if form-items are empty
            if (this.email) {a
                postBody.email = this.email
                this.email = '';
            }
            if (this.password) {
                postBody.password = this.password
                this.password = '';
            }
            if (this.name) {
                postBody.name = this.name
                this.name = '';
            }

            axios.post('/users', {
                id: postBody.id,
                email: postBody.email,
                password: postBody.password,
                name: postBody.name
            })
            .then(response => {
                this.errorMessage = '';
                this.popup = ''
            })
            .catch(e => {
                this.errorMessage = e.toString();
                this.errors.push(e)
            })
        },
        addUser() {
            var postBody= [];

            //check if form-items are empty
            if (this.email) {
                postBody.email = this.email
                this.email = '';
            }
            if (this.password) {
                postBody.password = this.password
                this.password = '';
            }
            if (this.name) {
                postBody.name = this.name
                this.name = '';
            } else {
                postBody.name = '';
            }

            axios.post('/users', {
                    email: postBody.email,
                    password: postBody.password,
                    name: postBody.name
                })
                .then(response => {
                    this.errorMessage = '';
                    this.popup = '';
                    this.currUser= '';
                    this.getUsers();
                })
                .catch(e => {
                    this.errorMessage = e.toString();
                    this.errors.push(e)
                })
        },
        deleteUser() {
            var route= '/users/' + this.currUser._id;
            axios.delete(route, {})
            .then(response => {
                this.errorMessage = '';
                this.currUser = '';
                this.popup = '';
                this.getUsers();
            })
            .catch(e => {
                this.errorMessage = e.toString();
                this.errors.push(e)
            })
        },
        openEdit(c) {
            this.popup = 1;
            this.currUser = currUser

        },
        openDelete(c) {
            this.popup = 2;
            this.currUser = currUser
        }
    },
    watch: {
        view: function() {
            this.getUsers();
            return this.view;
        }
    },
    beforeMount(){
        this.getUsers();
    }
});
