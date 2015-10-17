
Flask API "DOs"
*    Implement API versions as blueprints
     This way your compatibility-breaking changes are modularized and separated by url.

*    Use signals and mocks for testing
     Signals and mocks make unit testing easy if you modularize your API carefully

*    Use decorators as a code-reuse pattern
     Flask is flexible, so use decorators to abstract out reusable patterns.

*    Use Flask's custom error handler capability

     The one feature that nobody uses, but everyone should. You should almost never use abort in your API endpoints.


Flask API "DON'Ts"

*   DON'T use your version control system to version your APIs
    You'll just wind up with a bunch of incompatible code branches that you might not be able to merge.

*   DON'T write endpoints you can't test
    Flask makes it easy to test your endpoints using signals, so you have no excuse.

*   DON'T use lots of extensions
    For any application of sufficient complexity, you will outgrow your extensions. The one exception: when you write your own.


