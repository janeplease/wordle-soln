from output_from_sevice import OutputFromService

outputFromService = OutputFromService

outputFromService.initialize_session(outputFromService)

print(outputFromService.session_begin)
print(len(outputFromService.potential_words))

outputFromService.func(outputFromService)