class CustomGraphQLMiddleware:
    def resolve(self, next, root, info, **args):
        try:
            result = next(root, info, **args)
            return result
        
        except Exception as e:
            raise e
