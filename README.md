# OpenSimulationInterface.CSharp

This repository contains the build pipeline to generate C# code for the OpenSimulationInterface (OSI) protocol buffers. 
The generated code is packaged as a NuGet package `OpenSimulationInterface.CSharp` and published on NuGet.

## Building the Project locally

1. Make sure to have python 3 installed on your machine.

2. Clone the repository and navigate to the root directory.

3. Add the following code to the `.csproj` file to generate the C# files from the `.proto` files. This makes sure, that the required version dependencies are installed and the C# files are generated from the `.proto` files before building the project.

```xml
	<Target Name="ProtobufCompile" BeforeTargets="BeforeBuild">
		<Exec Command="python setup.py ./open-simulation-interface/osi_version.proto.in ./open-simulation-interface/VERSION ./open-simulation-interface/osi_version.proto" />
		<Exec Command="protoc --proto_path=%userprofile%\.nuget\packages\google.protobuf.tools\3.26.1\tools --proto_path=open-simulation-interface --csharp_out=. open-simulation-interface\*.proto" />
	</Target>
```

4. Build the project.

## Usage

After installing the `OpenSimulationInterface.CSharp` package, you can use the generated classes in your C# projects. Here is an example:


```csharp
using Osi3;
using Google.Protobuf;

public class Program
{
    static void Main(string[] args)
    {
        // Create an instance of GroundTruth and initialize properties
        GroundTruth groundTruth = new GroundTruth
        {
            Version = new InterfaceVersion
            {
                VersionMajor = 3, 
                VersionMinor = 7, 
                VersionPatch = 0
            },

            Timestamp = new Timestamp
            {
                Seconds = 1234567890, 
                Nanos = 123456789
            },

            HostVehicleId = new Identifier
            {
                Value = 12345
            },
            
            // Add other properties as needed
        };

        // Serialize to protobuf binary
        byte[] serializedData = groundTruth.ToByteArray();
        Console.WriteLine($"Serialized GroundTruth to {serializedData.Length} bytes.");

        // Deserialize from protobuf binary
        GroundTruth? deserializedData = GroundTruth.Parser.ParseFrom(serializedData);
        Console.WriteLine($"Deserialized GroundTruth with version " +
                          $"{deserializedData.Version.VersionMajor}" +
                          $".{deserializedData.Version.VersionMinor}" +
                          $".{deserializedData.Version.VersionPatch}.");

        Console.ReadKey(); // Prevent console from closing
    }
}
```
