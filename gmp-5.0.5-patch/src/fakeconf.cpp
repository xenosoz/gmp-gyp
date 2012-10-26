#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

string data[] = {
	"@HAVE_HOST_CPU_FAMILY_power@", "0",
	"@HAVE_HOST_CPU_FAMILY_powerpc@", "0",
	"@GMP_LIMB_BITS@", "32",
	"@GMP_NAIL_BITS@", "0",
	"@DEFN_LONG_LONG_LIMB@", "/* #undef _LONG_LONG_LIMB */",
	"@LIBGMP_DLL@", "0",
	"@CC@", "",
	"@CFLAGS@", "",

	"#undef HAVE_HOST_CPU_FAMILY_x86", "#define HAVE_HOST_CPU_FAMILY_x86 1",
	"#undef GMP_MPARAM_H_SUGGEST", "#define GMP_MPARAM_H_SUGGEST \"./mpn/x86/p6/gmp-mparam.h\"",
	"#undef HAVE_ALLOCA", "#define HAVE_ALLOCA 1",
	"#undef HAVE_CALLING_CONVENTIONS", "#define HAVE_CALLING_CONVENTIONS 1",
	"#undef HAVE_CLOCK", "#define HAVE_CLOCK 1",
	"#undef HAVE_DECL_FGETC", "#define HAVE_DECL_FGETC 1",
	"#undef HAVE_DECL_FSCANF", "#define HAVE_DECL_FSCANF 1",
	"#undef HAVE_DECL_OPTARG", "#define HAVE_DECL_OPTARG 0",
	"#undef HAVE_DECL_UNGETC", "#define HAVE_DECL_UNGETC 1",
	"#undef HAVE_DECL_VFPRINTF", "#define HAVE_DECL_VFPRINTF 1",
	"#undef HAVE_DOUBLE_IEEE_LITTLE_ENDIAN", "#define HAVE_DOUBLE_IEEE_LITTLE_ENDIAN 1",
	"#undef HAVE_FCNTL_H", "#define HAVE_FCNTL_H 1",
	"#undef HAVE_GETPAGESIZE", "#define HAVE_GETPAGESIZE 1",
	"#undef HAVE_INTMAX_T", "#define HAVE_INTMAX_T 1",
	"#undef HAVE_LIMB_LITTLE_ENDIAN", "#define HAVE_LIMB_LITTLE_ENDIAN 1",
	"#undef HAVE_LOCALECONV", "#define HAVE_LOCALECONV 1",
	"#undef HAVE_LOCALE_H", "#define HAVE_LOCALE_H 1",
	"#undef HAVE_LONG_DOUBLE", "#define HAVE_LONG_DOUBLE 1",
	"#undef HAVE_MEMORY_H", "#define HAVE_MEMORY_H 1",
	"#undef HAVE_MEMSET", "#define HAVE_MEMSET 1",
	"#undef HAVE_MPROTECT", "#define HAVE_MPROTECT 1",
	"#undef HAVE_POPEN", "#define HAVE_POPEN 1",
	"#undef HAVE_PTRDIFF_T", "#define HAVE_PTRDIFF_T 1",
	"#undef HAVE_SPEED_CYCLECOUNTER", "#define HAVE_SPEED_CYCLECOUNTER 2",
	"#undef HAVE_STDARG", "#define HAVE_STDARG 1",
	"#undef HAVE_STDINT_H", "#define HAVE_STDINT_H 1",
	"#undef HAVE_STDLIB_H", "#define HAVE_STDLIB_H 1",
	"#undef HAVE_STRCHR", "#define HAVE_STRCHR 1",
	"#undef HAVE_STRINGIZE", "#define HAVE_STRINGIZE 1",
	"#undef HAVE_STRING_H", "#define HAVE_STRING_H 1",
	"#undef HAVE_STRNLEN", "#define HAVE_STRNLEN 1",
	"#undef HAVE_STRTOUL", "#define HAVE_STRTOUL 1",
	"#undef HAVE_SYS_STAT_H", "#define HAVE_SYS_STAT_H 1",
	"#undef HAVE_SYS_TIME_H", "#define HAVE_SYS_TIME_H 1",
	"#undef HAVE_SYS_TYPES_H", "#define HAVE_SYS_TYPES_H 1",
	//"#undef HAVE_UNISTD_H", "#define HAVE_UNISTD_H 1",
	"#undef LSYM_PREFIX", "#define LSYM_PREFIX \"L\"",
	"#undef PACKAGE", "#define PACKAGE \"gmp\"",
	"#undef PROTOTYPES", "#define PROTOTYPES 1",
	"#undef RETSIGTYPE", "#define RETSIGTYPE void",
	"#undef STDC_HEADERS", "#define STDC_HEADERS 1",
	"#undef TIME_WITH_SYS_TIME", "#define TIME_WITH_SYS_TIME 1",
	"#undef VERSION", "#define VERSION \"5.0.5\"",
	"#undef WANT_FFT", "#define WANT_FFT 1",
	"#undef WANT_TMP_ALLOCA", "#define WANT_TMP_ALLOCA 1",	
	"#undef HAVE_MEMORY_H", "#define HAVE_MEMORY_H 1",
	"#undef HAVE_MEMSET", "#define HAVE_MEMSET 1",

	"#undef inline", "#define inline __inline",

	"#undef SIZEOF_UNSIGNED_LONG", "",
};
const size_t size_data = sizeof(data)/sizeof(data[0]);

void replace_all_dirty(std::string& str, const std::string& from, const std::string& to)
{
	if(from.empty()) {
		return;
	}
	size_t last = 0;
	while(true)
	{
		last = str.find(from, last);
		if(last == string::npos) {
			break;
		}
		size_t end = last + from.length();
		if(end < str.length() && str[end] == '_') {
			// quick and dirty solution to "#undef PACKAGE" vs "#undef PACKAGE_*".
			last += 1;
			continue;
		}
		str.replace(last, from.length(), to);
		last += to.length();
	}
}

int main(int argc, char* argv[])
{
	if(argc < 3) {
		cerr << "usage: " << endl;
		cerr << "  " << argv[0] << " {source} {destination}" << endl;
		return -1;
	}

	for(size_t i = 0; i < size_data; i += 2) {
		if(data[i] == "#undef SIZEOF_UNSIGNED_LONG") {
			stringstream ss;
			ss << "#define SIZEOF_UNSIGNED_LONG " << sizeof(unsigned long);
			data[i+1] = ss.str();
		}
	}

	const string path_src(argv[1]);
	const string path_dst(argv[2]);

	ifstream file_src(path_src);
	ofstream file_dst(path_dst);

	string line;
	while(getline(file_src, line))
	{
		for(size_t i = 0; i < size_data; i += 2) {
			replace_all_dirty(line, data[i], data[i+1]);
		}
		file_dst << line << endl;
	}
	return 0;
}